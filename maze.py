#! /usr/bin/env python3
# coding: utf-8

from framework import laby
import pygame


def main():
    start = True
    welcome = True
    create_player = True
    while start:
        pygame.time.Clock().tick(100)
        if create_player:
            player = laby.Laby()
            create_player = False
            
        if welcome:
            for event in pygame.event.get():
                player.graphics.welcome_game()
                if event.type == pygame.QUIT:
                    start = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                    elif event.key == pygame.K_RETURN:
                        welcome = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    welcome = False
        

        if player.user.dead is False and welcome is False and player.user.end is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                    if event.key == pygame.K_RIGHT:
                        player.user.move("RIGHT")
                    if event.key == pygame.K_LEFT:
                        player.user.move("LEFT")
                    if event.key == pygame.K_UP:
                        player.user.move("UP")
                    if event.key == pygame.K_DOWN:
                        player.user.move("DOWN")
                player.graphics.update_views_map()

        if player.user.dead and player.user.end:
            for event in pygame.event.get():
                player.graphics.lose_game()
                if event.type == pygame.QUIT:
                    start = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                    elif event.key == pygame.K_RETURN:
                        player.user.end = False
                        create_player = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    player.user.end = False
                    create_player = True

        if player.user.dead is False and player.user.end:
            for event in pygame.event.get():
                player.graphics.win_game()
                if event.type == pygame.QUIT:
                    start = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        start = False
                    elif event.key == pygame.K_RETURN:
                        player.user.end = False
                        create_player = True
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    player.user.end = False
                    create_player = True
    
if __name__ == "__main__":
    main()
