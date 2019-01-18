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
        with open('map/maps.txt', 'r') as maps:
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

                if not self.items :
                    self.end_player = True
                else:
                    print("vous n'avez pas récupéré tout les objets")
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
            if self.verif_position(x,y) == False:
                x -=1
                self.print_map(self.position)
            else:
                self.position = (x,y)
                self.print_map(self.position)

        elif direction == "z":
            x, y = self.position
            x -=1
            if self.verif_position(x,y) == False:
                x +=1
                self.print_map(self.position)
            else:

                self.position = (x,y)
                self.print_map(self.position)

        elif direction == "q":
            x, y = self.position
            y -=1
            if self.verif_position(x,y) == False:
                y +=1
                self.print_map(self.position)
            else:
                self.position = (x,y)
                self.print_map(self.position)
        elif direction == "d":
            x, y = self.position
            y +=1
            if self.verif_position(x,y) == False:
                y -=1
                self.print_map(self.position)
            else:
                self.position = (x,y)
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

    def verif_position(self,position_x, position_y):
        if position_x < 0 or position_x > self.x or position_y < 0 or position_y > self.y:
            print("Vous ne pouvez pas sortir du labyrinthe")
            return False
        
        elif ((position_x, position_y) in self.wall):
            print("Vous ne pouvez pas traverser les murs")
            return False
        elif ((position_x, position_y) in self.items):
            index = self.items.index((position_x, position_y))
            r = self.items.pop(index)
            self.road.append(r)
            print("vous avez récupérer un objet")
            return True
        else:
            return True


def main():
    lab = Labyrinth()
    lab.print_map(lab.position)

    while lab.end_player == False:
        direction = input("enter: ")
        lab.deplacement(direction.lower())

    if lab.end_player == True and direction != "exit":
        print("!!!!!!! Bravo vous êtes vainqueur !!!!!!!")
    else:
        print("vous êtes partit avant la fin, Dommage !!!")

main()