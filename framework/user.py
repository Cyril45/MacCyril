#! /usr/bin/env python3
# coding: utf-8


class User:
    def __init__(self, laby):
        self.objects_collect = 0
        self.end = False
        self.dead = False

        self.position = ()
        self.laby = laby

    def move(self, direction):
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
