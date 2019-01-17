class Labyrinth:
    def __init__(self):
        self.full_map = [] #map with all the items in place.
        self.items = [] # List of position of items
        self.end = [] #end position
        self.start = [] #start position
        self.road = [] # list of position of roads
        self.wall = [] # list of position of wall

        self.x = int
        self.y = int

        self.load_data_map()
        self.create_blank_map()


    def load_data_map(self):
        temp = int
        with open('maps.txt', 'r') as maps:
            for x, line in enumerate(maps):
                for y, case in enumerate(line.strip()):
                    temp = x , y
                    self.x = x
                    self.y = y
                    if case == " ":
                        self.road.append((x, y))
                    elif case == "D": 
                        self.start.append((x, y))
                    elif case == "A": 
                        self.end.append((x, y))
                    elif case =="O":
                        self.items.append((x, y))
                    else:
                        self.wall.append((x, y))

    def create_blank_map(self):
        self.full_map= [[""]]*(self.x+1)
        numberliste = 0
        while numberliste < (self.x+1):
            self.full_map[numberliste] = [""]*(self.y+1)
            numberliste +=1
        
    def load_data_user(self,position):
        for z in self.items:
            x,y =z
            if position == z:
                self.full_map[x][y] = "M"
            else:
                self.full_map[x][y]="O"
        for z in self.end:
            x,y =z
            if position == z:
                self.full_map[x][y] = "M"
            else:
                self.full_map[x][y] = "A"
        for z in self.start:
            x,y =z
            if position == z:
                self.full_map[x][y] = "M"
            else:
                self.full_map[x][y] = "D"

        for z in self.road:
            x,y =z
            if position == z:
                self.full_map[x][y] = "M"
            else:
                self.full_map[x][y] = " "
        for z in self.wall:
            x,y =z
            self.full_map[x][y] = "#"
    
    def print_map(self, player_location):
        self.load_data_user(player_location)
        for a in self.full_map:
            print(a)



def main():
    lab = Labyrinth()
    player_location = (3, 2)
    lab.print_map(player_location)

main()
