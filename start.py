#! /usr/bin/env python3
# coding: utf-8

from framework import laby
import pygame


def main():
    start = True
    welcome = True
    create_player = False
    player = laby.Laby()
    while start:
        pygame.time.Clock().tick(20)
        if create_player:
            player = laby.Laby()
            create_player = False

        if welcome:
            welcome, start = player.graphics.welcome_game(welcome, start)

        if player.user.dead is False \
           and welcome is False and player.user.end is False:
            start = player.graphics.play_game(start)

        if player.user.dead and player.user.end:
            start, create_player = \
              player.graphics.lose_game(start, create_player)

        if player.user.dead is False and player.user.end:
            start, create_player = \
              player.graphics.win_game(start, create_player)


if __name__ == "__main__":
    main()
