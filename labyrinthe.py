import functions
def main():
    player = functions.Var_init()
    functions.Initialize_map(player)
    print(player.message)
    functions.Print_map(player).printt(player.position)

    while player.end_player == False:
        direction = input("enter: ")
        functions.Move_map(player).movement(direction.lower())

    if player.end_player == True and direction != "exit":
        print("!!!!!!! Bravo you are victorious !!!!!!!")
    else:
        print("You left before the end, Damage !!!")

main()