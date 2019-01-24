#! /usr/bin/env python3
# coding: utf-8

from framework import laby


def main():

    player = laby.Laby()
    while player.user.end is False:
        print(player.user.objects_collect, player.objects_numbers)
        player.view_map()
        direction = input("enter: ")
        player.user.move(direction)

    player.view_map()

    if player.user.end and direction != "exit" and player.user.dead is False:
        print("You win")

    elif player.user.dead:
        print("You lose")

    else:
        print("You have to leave")


if __name__ == "__main__":
    main()
