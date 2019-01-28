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
            if self.lab.full_map[random_x][random_y] == "_" and \
               self.lab.full_map[random_x][random_y] not in ("D", "A"):
                self.lab.full_map[random_x][random_y] = "O" + str(i)
                i += 1

    def objectInCase(self, news_x, news_y):
        if self.lab.full_map[news_x][news_y] in ("O0", "O1", "O2"):
                self.lab.user.objects_collect += 1
                self.lab.full_map[news_x][news_y] == "_"
