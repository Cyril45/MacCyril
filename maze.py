import functions


def main():

    player = functions.Var_init()
    functions.Initialize_map(player)
    print(player.menu)
    functions.Print_map(player).printt(player.position)

    while player.end_player is False:
        direction = input("enter: ")
        functions.Move_map(player).move(direction.lower())

    if player.end_player is True and \
       direction != "exit" and player.dead is False:
        print(player.message_5)

    elif player.dead is True:
        print(player.message_6)

    else:
        print(player.message_7)


main()
