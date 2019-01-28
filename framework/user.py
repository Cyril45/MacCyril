#! /usr/bin/env python3
# coding: utf-8


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
        x, y = self.position
        if direction == "DOWN":
            x += 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "UP":
            x -= 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "LEFT":
            y -= 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "RIGHT":
            y += 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
