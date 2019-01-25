#! /usr/bin/env python3
# coding: utf-8

import pygame
from config import constants

class Graphics:

    def __init__(self, laby):
        self.laby = laby

        #Initialize window
        pygame.init()
        self.size_image = constants.size_image
        self.width = (self.laby.y+1) * self.size_image
        self.height = (self.laby.x+1) * self.size_image
        self.window = pygame.display.set_mode((self.width, self.height+60))
        pygame.key.set_repeat(400, 30)
        pygame.display.set_caption(constants.windows_title)
        icone = pygame.image.load(constants.icone).convert_alpha()
        pygame.display.set_icon(icone)

        #Initialize images
        self.banner = pygame.image.load(constants.banner)
        self.banner =  pygame.transform.scale(self.banner, (self.width, self.height+60))

        self.win = pygame.image.load(constants.win).convert_alpha()
        self.win =  pygame.transform.scale(self.win, (self.width, self.height+60))

        self.lose = pygame.image.load(constants.lose).convert_alpha()
        self.lose =  pygame.transform.scale(self.lose, (self.width, self.height+60))

        self.background = pygame.image.load(constants.background).convert()
        self.background =  pygame.transform.scale(self.background, (self.size_image, self.size_image))

        self.walls = pygame.image.load(constants.walls).convert()
        self.walls = pygame.transform.scale(self.walls, (self.size_image, self.size_image))

        self.hero = pygame.image.load(constants.hero).convert_alpha()
        self.hero = pygame.transform.scale(self.hero, (self.size_image, self.size_image))

        self.start = pygame.image.load(constants.start).convert_alpha()
        self.start = pygame.transform.scale(self.start, (self.size_image, self.size_image))

        self.guardian = pygame.image.load(constants.guardian).convert_alpha()
        self.guardian = pygame.transform.scale(self.guardian, (self.size_image, self.size_image))

        self.object0 =  pygame.image.load(constants.object0).convert_alpha()
        self.object0 = pygame.transform.scale(self.object0, (self.size_image, self.size_image))

        self.object1 =  pygame.image.load(constants.object1).convert_alpha()
        self.object1 = pygame.transform.scale(self.object1, (self.size_image, self.size_image))

        self.object2 =  pygame.image.load(constants.object2).convert_alpha()
        self.object2 = pygame.transform.scale(self.object2, (self.size_image, self.size_image))

    def welcome_game(self):
        self.window.blit(self.banner,(0,0))
        pygame.display.flip()
     

    def win_game(self):
        self.window.blit(self.win,(0,0))
        pygame.display.flip()
    
    def lose_game(self):
        self.window.blit(self.lose,(0,0))
        pygame.display.flip()


    def update_views_map(self):
        self.window.fill((30, 28, 30))
        for x, line in enumerate(self.laby.full_map):
            for y, case in enumerate(line):
                x_sprite = x * self.size_image
                y_sprite = y * self.size_image
                if case == "A":
                    self.window.blit(self.background, (y_sprite, x_sprite))
                    self.window.blit(self.guardian, (y_sprite,  x_sprite))
                if case == "#":
                    self.window.blit(self.walls, (y_sprite, x_sprite))
                if case == "M":
                    self.window.blit(self.background, (y_sprite, x_sprite))
                    self.window.blit(self.hero, (y_sprite, x_sprite))
                if case == "_":
                    self.window.blit(self.background, (y_sprite, x_sprite))
                if case == "O0":
                    self.window.blit(self.background, (y_sprite, x_sprite))
                    self.window.blit(self.object0, (y_sprite, x_sprite))
                if case == "O1":
                    self.window.blit(self.background, (y_sprite, x_sprite))
                    self.window.blit(self.object1, (y_sprite, x_sprite))
                if case == "O2":
                    self.window.blit(self.background, (y_sprite, x_sprite))
                    self.window.blit(self.object2, (y_sprite, x_sprite))
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Items recovered : " + str(self.laby.user.objects_collect), True, (255, 255, 255))
        self.window.blit(text,(15,self.height))

        pygame.display.flip()

