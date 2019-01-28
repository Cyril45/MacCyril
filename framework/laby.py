#! /usr/bin/env python3
# coding: utf-8

from framework import objects
from framework import user
from views import graphics


class Laby:
    """This class initializes all maze data"""
    def __init__(self):
        """This manufacturer initializes the information necessary for the
        maze as well as the objects necessary for its proper functioning."""
        self.full_map = []  # map with all the items in place.
        self.objects_numbers = 3
        self.x = None
        self.y = None

        self.user = user.User(self)
        self.objects = objects.Objects(self)
        self.load_data_map()
        self.objects.random_objects()
        self.graphics = graphics.Graphics(self)

    def load_data_map(self):
        """This method retrieves map information"""
        with open("map/maps.txt") as maps:
            for x, line in enumerate(maps):
                self.x = x
                self.full_map.insert(x, [])
                for y, case in enumerate(line.strip()):
                    self.y = y
                    if case == "D":
                        self.full_map[x].insert(y, "M")
                        self.user.position = (x, y)
                    elif case == "A":
                        self.full_map[x].insert(y, "A")
                    elif case == "_":
                        self.full_map[x].insert(y, "_")
                    elif case == "#":
                        self.full_map[x].insert(y, "#")

    def check_position(self, position):
        """ This method checks if the position requested by the player is
        contained in the map """
        x, y = position
        try:
            if self.full_map[x][y] not in "#" \
              and x <= self.x and y <= self.y and x >= 0 and y >= 0:
                return True
            else:
                return False
        except IndexError:
            return False

    def modify_map(self, position):
        """ This method modifies the map after the player moves."""
        old_x, old_y = self.user.position
        news_x, news_y = position
        if self.check_position(position):
            self.objects.objectInCase(news_x, news_y)
            if self.full_map[news_x][news_y] == "A":
                if self.user.objects_collect < self.objects_numbers:
                    self.user.dead = True
                self.user.end = True
            self.full_map[old_x][old_y] = "_"
            self.full_map[news_x][news_y] = "M"
            self.user.position = position
