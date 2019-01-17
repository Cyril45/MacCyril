class Labyrinth:
    def __init__(self):
        self.full_map = [] #map with all the items in place.
        self.items = [] # List of position of items
        self.end = [] #end position
        self.start = [] #start position
        self.road = [] # list of position of roads
        self.wall = [] # list of position of wall
        self.position = ()
        self.end_player = False
        self.x = int
        self.y = int

        self.load_data_map()
        self.create_blank_map()


    def load_data_map(self):
        with open('maps.txt', 'r') as maps:
            for x, line in enumerate(maps):
                for y, case in enumerate(line.strip()):
                    self.x = x
                    self.y = y
                    if case == " ":
                        self.road.append((x, y))
                    elif case == "D": 
                        self.start.append((x, y))
                        self.position = (x, y)
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
                self.end_player = True
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
    
    def print_map(self, position):
        self.load_data_user(position)
        for a in self.full_map:
            print(a)

    def deplacement(self, direction):
        if direction == "s":
            x, y = self.position
            x +=1
            self.position = (x,y)
            try:
                self.position != self.wall.index(self.position)
                x, y = self.position
                x -=1
                self.position = (x,y)
                self.print_map(self.position)
                print("Vous ne pouvea pas traversée les murs")
            except:
                self.print_map(self.position)

        elif direction == "z":
            x, y = self.position
            x -=1
            self.position = (x,y)
            try:
                self.position != self.wall.index(self.position)
                x, y = self.position
                x +=1
                self.position = (x,y)
                self.print_map(self.position)
                print("Vous ne pouvea pas traversée les murs")
            except:
                self.print_map(self.position)

        elif direction == "q":
            x, y = self.position
            y -=1
            self.position = (x,y)
            try:
                self.position != self.wall.index(self.position)
                x, y = self.position
                y +=1
                self.position = (x,y)
                self.print_map(self.position)
                print("Vous ne pouvea pas traversée les murs")
            except:
                self.print_map(self.position)
        elif direction == "d":
            x, y = self.position
            y +=1
            self.position = (x,y)
            try:
                self.position != self.wall.index(self.position)
                x, y = self.position
                y -=1
                self.position = (x,y)
                self.print_map(self.position)
                print("Vous ne pouvea pas traversée les murs")
            except:
                self.print_map(self.position)

        elif direction == "exit":
            self.end_player = True

        else:

            print("Merci d'utilser les touches suivantes\n \
            z : pour un déplacement ver le haut\n \
            s : pour un déplacement ver le bas\n \
            q : pour un déplacement ver la gauche\n \
            d : pour un déplacement ver la droite\n\n \
            Exit : pour quitter")
            self.print_map(self.position)

def main():
    lab = Labyrinth()
    lab.print_map(lab.position)

    while lab.end_player == False:
        direction = input("enter: ")
        lab.deplacement(direction.lower())

    if lab.end_player == True and direction != "exit":
        print("!!!!!!! Bravo vous êtes vainqueur !!!!!!!")
    else:
        print("vous étes partit avant la fin, Dommage !!!")

main()