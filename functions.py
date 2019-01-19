class Var_init:

    def __init__(self):
        self.full_map = []  # map with all the items in place.
        self.items = []  # List of position of items
        self.road = []  # list of position of roads
        self.wall = []  # list of position of wall
        self.position = () # tuple contains player position
        self.end = ()  # tuple contains end position
        self.start = ()  # tuple contains start position
        self.message = ("\
            z : for an upward movement\n \
            s : for a downward movement\n \
            q : for a movement to the left\n \
            d : for movement to the right\n\n \
            Exit to leave")
        self.end_player = False
        self.x = int
        self.y = int


class Initialize_map:
    def __init__(self, player):
        self.player = player
        self.load_data_map()
        self.create_blank_map()

    def load_data_map(self):
        with open("map/maps.txt", 'r') as maps:
            for x, line in enumerate(maps):
                for y, case in enumerate(line.strip()):
                    self.player.x = x
                    self.player.y = y

                    if case == " ":
                        self.player.road.append((x, y))

                    elif case == "D":
                        self.player.start = (x, y)
                        self.player.position = (x, y)

                    elif case == "A":
                        self.player.end = (x, y)

                    elif case == "O":
                        self.player.items.append((x, y))

                    else:
                        self.player.wall.append((x, y))

    def create_blank_map(self):
        self.player.full_map = [[""]]*(self.player.x+1)
        numberlist = 0

        while numberlist < (self.player.x+1):
            self.player.full_map[numberlist] = [""]*(self.player.y+1)
            numberlist += 1


class Move_map:
    def __init__(self, player):
        self.player = player

    def movement(self, direction):
        if direction == "s":
            x, y = self.player.position
            x += 1
            if self.check_position(x, y) is False:
                x -= 1
                Print_map(self.player).printt(self.player.position)
            else:
                self.player.position = (x, y)
                Print_map(self.player).printt(self.player.position)

        elif direction == "z":
            x, y = self.player.position
            x -= 1
            if self.check_position(x, y) is False:
                x += 1
                Print_map(self.player).printt(self.player.position)
            else:
                self.player.position = (x, y)
                Print_map(self.player).printt(self.player.position)

        elif direction == "q":
            x, y = self.player.position
            y -= 1
            if self.check_position(x, y) is False:
                y += 1
                Print_map(self.player).printt(self.player.position)
            else:
                self.player.position = (x, y)
                Print_map(self.player).printt(self.player.position)

        elif direction == "d":
            x, y = self.player.position
            y += 1
            if self.check_position(x, y) is False:
                y -= 1
                Print_map(self.player).printt(self.player.position)
            else:
                self.player.position = (x, y)
                Print_map(self.player).printt(self.player.position)

        elif direction == "exit":
            self.player.end_player = True

        else:
            print("Thank you for using the following touches")
            print(self.player.message)
            Print_map(self.player).printt(self.player.position)

    def check_position(self, position_x, position_y):
        if position_x < 0 or position_y < 0 or \
         position_x > self.player.x or position_y > self.player.y:
            print("You can’t get out of the maze")
            return False

        elif ((position_x, position_y) in self.player.wall):
            print("You can’t cross the walls")
            return False

        elif ((position_x, position_y) in self.player.items):
            index = self.player.items.index((position_x, position_y))
            r = self.player.items.pop(index)
            self.player.road.append(r)
            print("You got back an object")
            return True

        else:
            return True


class Print_map:
    def __init__(self, player):
        self.player = player

    def printt(self, position):
        self.load_data_user(position)

        for a in self.player.full_map:
            print(a)

    def load_data_user(self, position):
        if position == self.player.start:
            x, y = self.player.start
            self.player.full_map[x][y] = "M"
        else:
            x, y = self.player.start
            self.player.full_map[x][y] = " "

        if position == self.player.end:
            x, y = self.player.end
            self.player.full_map[x][y] = "M"
            if not self.player.items:
                self.player.end_player = True
            else:
                print("you have not recovered all the objects")
        else:
            x, y = self.player.end
            self.player.full_map[x][y] = "A"

        for z in self.player.items:
            x, y = z
            if position == z:
                self.player.full_map[x][y] = "M"
            else:
                self.player.full_map[x][y] = "O"

        for z in self.player.road:
            x, y = z
            if position == z:
                self.player.full_map[x][y] = "M"
            else:
                self.player.full_map[x][y] = " "

        for z in self.player.wall:
            x, y = z
            self.player.full_map[x][y] = "#"
