#! /usr/bin/env python3
# coding: utf-8

from framework import objects
from framework import user

class Laby:
    def __init__(self):
        self.full_map = []  # map with all the items in place.
        self.objects_numbers = 3
        self.x = None
        self.y = None


        self.user = user.User(self)
        self.objects = objects.Objects(self)


        self.load_data_map()
        self.objects.random_objects()

    def load_data_map(self):
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
                    elif case == " ":
                        self.full_map[x].insert(y, " ")
                    elif case == "#":
                        self.full_map[x].insert(y, "#")

    def check_position(self, position):
        x, y = position
        if self.full_map[x][y] == " " or \
           self.full_map[x][y] == "A" or self.full_map[x][y] == "O":
            return True
        else:
            return False

    def modify_map(self, position):
        old_x, old_y = self.user.position
        news_x, news_y = position
        if self.check_position(position):
            self.objects.objectInCase(news_x, news_y)
            if self.full_map[news_x][news_y] == "A":
                if self.user.objects_collect < self.objects_numbers:
                    self.user.dead = True
                self.user.end = True
            self.full_map[old_x][old_y] = " "
            self.full_map[news_x][news_y] = "M"
            self.user.position = position

    def view_map(self):
        for a in self.full_map:
            print(a)
