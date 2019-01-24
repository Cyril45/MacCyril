#! /usr/bin/env python3
# coding: utf-8

from framework import laby

import pygame

def main():
    player = laby.Laby()
    player.graphics.welcome_game()
    while player.user.end is False:
        pygame.time.Clock().tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.user.move("EXIT")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    player.user.move("EXIT")
                if event.key == pygame.K_RIGHT:
                    player.user.move("RIGHT")
                if event.key == pygame.K_LEFT:
                    player.user.move("LEFT")
                if event.key == pygame.K_UP:
                    player.user.move("UP")
                if event.key == pygame.K_DOWN:
                    player.user.move("DOWN")
        player.graphics.update_views()





    #     print(player.user.objects_collect, player.objects_numbers)
    #     player.view_map()
    #     direction = input("enter: ")
    #     player.user.move(direction)

    # player.view_map()

    # if player.user.end and direction != "exit" and player.user.dead is False:
    #     print("You win")

    # elif player.user.dead:
    #     print("You lose")

    # else:
    #     print("You have to leave")


if __name__ == "__main__":
    main()
