#! /usr/bin/env python3
# coding: utf-8

"""This module contains all classes for the player"""

class User:
    """This class creates a player"""
    def __init__(self, laby):
        """ Initializes the number of objects that the user has collected,
        if he finishes the game, if he dies, his position and retrieves the
        information from Laby.py to send the map changes"""
        self.objects_collect = 0
        self.end = False
        self.dead = False

        self.position = ()
        self.laby = laby

    def move(self, direction):
        """This method changes the player’s position"""
        x_axis, y_axis = self.position
        if direction == "DOWN":
            x_axis += 1
            news_pos = (x_axis, y_axis)
            self.laby.modify_map(news_pos)
        elif direction == "UP":
            x_axis -= 1
            news_pos = (x_axis, y_axis)
            self.laby.modify_map(news_pos)
        elif direction == "LEFT":
            y_axis -= 1
            news_pos = (x_axis, y_axis)
            self.laby.modify_map(news_pos)
        elif direction == "RIGHT":
            y_axis += 1
            news_pos = (x_axis, y_axis)
            self.laby.modify_map(news_pos)
