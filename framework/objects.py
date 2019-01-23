#! /usr/bin/env python3
# coding: utf-8

from random import randint


class Objects:
    def __init__(self, lab):
        self.lab = lab

    def random_objects(self):
        i = 0
        while i < self.lab.objects_numbers:
            random_x = randint(0, self.lab.x)
            random_y = randint(0, self.lab.y)
            if self.lab.full_map[random_x][random_y] == " ":
                self.lab.full_map[random_x][random_y] = "O"
                i += 1

    def objectInCase(self, news_x, news_y):
        if self.lab.full_map[news_x][news_y] == "O":
                self.lab.user.objects_collect += 1
                self.lab.full_map[news_x][news_y] == " "
