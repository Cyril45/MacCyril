from random import randrange


class Var_init:
    def __init__(self):
        self.full_map = []  # map with all the items in place.
        self.items = []  # List of position of items
        self.road = []  # list of position of roads
        self.wall = []  # list of position of wall
        self.position = ()  # tuple contains player position
        self.end = ()  # tuple contains end position
        self.end_player = False
        self.dead = False
        self.items_collect = 0
        self.items_number = 3
        self.x = None
        self.y = None
        self.menu = ("\
            z : for an upward movement\n \
            s : for a downward movement\n \
            q : for a movement to the left\n \
            d : for movement to the right\n \
            exit to leave")
        self.message_1 = "Thank you for using the following touches"
        self.message_2 = "You can’t get out of the maze"
        self.message_3 = "You can’t cross the walls"
        self.message_4 = "You got back an object"
        self.message_5 = "!!!!!!! Bravo you are victorious !!!!!!!"
        self.message_6 = "You didn’t get all the objects you died"
        self.message_7 = "You left before the end, Damage !!!"


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
                        self.player.position = (x, y)
                        self.player.road.append((x, y))

                    elif case == "A":
                        self.player.end = (x, y)

                    else:
                        self.player.wall.append((x, y))

    def create_blank_map(self):
        self.player.full_map = [[""]]*(self.player.x+1)
        for i, v in enumerate(self.player.full_map):
            self.player.full_map[i] = [""]*(self.player.y+1)

        while self.player.items_number > len(self.player.items):
            pos_items = self.player.road.pop(randrange(0, len(self.player.road)))
            self.player.items.append(pos_items)


class Move_map:
    def __init__(self, player):
        self.player = player

    def move(self, direction):
        x, y = self.player.position
        if direction == "s" and self.check_position(x+1, y):
            x += 1

        elif direction == "z" and self.check_position(x-1, y):
            x -= 1

        elif direction == "q" and self.check_position(x, y-1):
            y -= 1

        elif direction == "d" and self.check_position(x, y+1):
            y += 1

        elif direction == "exit":
            self.player.end_player = True

        else:
            print(self.player.message_1)
            print(self.player.menu)

        self.player.position = (x, y)
        Print_map(self.player).printt(self.player.position)

    def check_position(self, position_x, position_y):
        if position_x < 0 or position_y < 0 \
          or position_x > self.player.x or position_y > self.player.y:
            print(self.player.message_2)
            return False

        elif ((position_x, position_y) in self.player.wall):
            print(self.player.message_3)
            return False

        elif ((position_x, position_y) in self.player.items):
            collect_pos = self.player.items.index((position_x, position_y))
            collect_values_items = self.player.items.pop(collect_pos)
            self.player.road.append(collect_values_items)
            self.player.items_collect += 1
            print(self.player.message_4)
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
        if position == self.player.position:
            x, y = position
            self.player.full_map[x][y] = "M"
        else:
            x, y = self.player.position
            self.player.full_map[x][y] = " "

        if position == self.player.end:
            x, y = position
            self.player.full_map[x][y] = "M"

            if not self.player.items:
                self.player.end_player = True
            else:
                self.player.end_player = True
                self.player.dead = True
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
