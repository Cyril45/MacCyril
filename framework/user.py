#! /usr/bin/env python3
# coding: utf-8



class User:
    def __init__(self, laby):
        self.objects_collect = 0
        self.end = False
        self.position = ()
        self.user = False
        self.dead = False
        self.laby = laby

    def move(self, direction):
        x, y = self.position
        if direction == "s":
            x += 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "z":
            x -= 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "q":
            y -= 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "d":
            y += 1
            news_pos = (x, y)
            self.laby.modify_map(news_pos)
        elif direction == "exit":
            self.end = True
