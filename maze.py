#! /usr/bin/env python3
# coding: utf-8

from framework import user


def main():

    player = user.User()
    while player.end is False:
        print(player.objects_collect, player.laby.objects_numbers)
        player.laby.view_map()
        direction = input("enter: ")
        player.move(direction)

    player.laby.view_map()

    if player.end and direction != "exit" and player.dead is False:
        print("You win")

    elif player.dead:
        print("You lose")

    else:
        print("You have to leave")


if __name__ == "__main__":
    main()
