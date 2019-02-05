#! /usr/bin/env python3
# coding: utf-8

"""This module contains all the classes dedicated to the maze"""

from framework.obj import Obj
from framework.user import User
from views.graphics import Graphics


class Laby:
    """This class initializes all maze data"""
    def __init__(self):
        """This manufacturer initializes the information necessary for the
        maze as well as the objects necessary for its proper functioning."""
        self.full_map = []  # map with all the items in place.
        self.list_objects = []
        self.objects_numbers = 3
        self.x_axis = None
        self.y_axis = None
        self.user = User(self)
        self.load_data_map()
        self.create_object()
        self.graphics = Graphics(self)

    def create_object(self):
        """This method creates objects and places it in a list"""
        i = 0
        for i in range(0, self.objects_numbers):
            self.list_objects.insert(i, Obj(self, i))

    def load_data_map(self):
        """This method retrieves map information"""
        with open("map/maps.txt") as maps:
            for x_axis, line in enumerate(maps):
                self.x_axis = x_axis
                self.full_map.insert(x_axis, [])
                for y_axis, case in enumerate(line.strip()):
                    self.y_axis = y_axis
                    if case == "D":
                        self.full_map[x_axis].insert(y_axis, "M")
                        self.user.position = (x_axis, y_axis)
                    elif case == "A":
                        self.full_map[x_axis].insert(y_axis, "A")
                    elif case == "_":
                        self.full_map[x_axis].insert(y_axis, "_")
                    elif case == "#":
                        self.full_map[x_axis].insert(y_axis, "#")

    def check_position(self, position):
        """ This method checks if the position requested by the player is
        contained in the map """
        x_axis, y_axis = position
        try:
            return bool(self.full_map[x_axis][y_axis] not in "#" \
              and x_axis <= self.x_axis and y_axis <= self.y_axis and x_axis >= 0 and y_axis >= 0)

        except IndexError:
            return False

    def object_in_case(self, news_x, news_y):
        """ This method checks if an object is in one box
        of the map and increments the player’s counter """
        if self.full_map[news_x][news_y] in ("O0", "O1", "O2"):
            self.user.objects_collect += 1
            self.full_map[news_x][news_y] = "_"

    def modify_map(self, position):
        """ This method modifies the map after the player moves."""
        old_x, old_y = self.user.position
        news_x, news_y = position
        if self.check_position(position):
            self.object_in_case(news_x, news_y)
            if self.full_map[news_x][news_y] == "A":
                if self.user.objects_collect < self.objects_numbers:
                    self.user.dead = True
                self.user.end = True
            else:
                self.full_map[old_x][old_y] = "_"
                self.full_map[news_x][news_y] = "M"
                self.user.position = position
