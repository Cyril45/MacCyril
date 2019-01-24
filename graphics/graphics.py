#! /usr/bin/env python3
# coding: utf-8

import pygame

class Graphics:

    def __init__(self, laby):
        pygame.init()
        self.laby = laby

        self.dim_sprite = 40

        self.largeur = (self.laby.y+1) * self.dim_sprite
        self.longueur = (self.laby.x+1) * self.dim_sprite

        self.fenetre = pygame.display.set_mode((self.largeur, self.longueur+50))
        self.welcome = pygame.image.load("ressource/tile-crusader-logo.png").convert()

        self.fond = pygame.image.load("ressource/sol.png").convert()
        self.fond =  pygame.transform.scale(self.fond, (40, 40))

        self.mur = pygame.image.load("ressource/mur.png").convert()
        self.mur = pygame.transform.scale(self.mur, (40, 40))

        self.perso = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        self.perso = pygame.transform.scale(self.perso, (40, 40))

        self.depart = pygame.image.load("ressource/sol.png").convert_alpha()
        self.depart = pygame.transform.scale(self.depart, (40, 40))

        self.arriver = pygame.image.load("ressource/Gardien.png").convert_alpha()
        self.arriver = pygame.transform.scale(self.arriver, (40, 40))

        self.objet0 =  pygame.image.load("ressource/aiguille.png").convert_alpha()
        self.objet0 = pygame.transform.scale(self.objet0, (40, 40))

        self.objet1 =  pygame.image.load("ressource/ether.png").convert_alpha()
        self.objet1 = pygame.transform.scale(self.objet1, (40, 40))

        self.objet2 =  pygame.image.load("ressource/tube_plastique.png").convert_alpha()
        self.objet2 = pygame.transform.scale(self.objet2, (40, 40))

    def welcome_game(self):
        self.fenetre.blit(self.welcome, (500,500))
        pygame.display.flip()

    def update_views(self):
        for x, line in enumerate(self.laby.full_map):
            for y, case in enumerate(line):
                x_sprite = x * self.dim_sprite
                y_sprite = y * self.dim_sprite
                if case == "A":
                    self.fenetre.blit(self.arriver, (y_sprite,  x_sprite))
                if case == "#":
                    self.fenetre.blit(self.mur, (y_sprite, x_sprite))
                if case == "D":
                    self.fenetre.blit(self.depart, (y_sprite, x_sprite))
                if case == "M":
                    self.fenetre.blit(self.perso, (y_sprite, x_sprite))
                if case == " ":
                    self.fenetre.blit(self.fond, (y_sprite, x_sprite))
                if case == "O0":
                    self.fenetre.blit(self.objet0, (y_sprite, x_sprite))
                if case == "O1":
                    self.fenetre.blit(self.objet1, (y_sprite, x_sprite))
                if case == "O2":
                    self.fenetre.blit(self.objet2, (y_sprite, x_sprite))

        pygame.display.flip()