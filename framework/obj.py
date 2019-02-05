#! /usr/bin/env python3
# coding: utf-8

"""This module contains all classes for objects"""

from random import randint


class Obj:
    """ The Obj class manages all events of objects in the map"""
    def __init__(self, lab, i):
        """ Retrieves information necessary for changes to objects in the map
        """
        self.laby = lab
        self.i = i
        self.random_objects()

    def random_objects(self):
        """This method randomly generates objects in available map spaces"""
        i = 0
        while i < 1:
            random_x = randint(0, self.laby.x_axis)
            random_y = randint(0, self.laby.y_axis)
            if self.laby.full_map[random_x][random_y] == "_":
                self.laby.full_map[random_x][random_y] = "O" + str(self.i)
                i += 1
