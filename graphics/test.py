#! /usr/bin/env python3
# coding: utf-8

import pygame

pygame.init()

fenetre = pygame.display.set_mode((640, 480),pygame.RESIZABLE) #initialise une fenetre de 640 x 480

fond = pygame.image.load("background.jpg").convert() # initialise une image de fond dans fond
perso = pygame.image.load("MacGyver.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(fond, (0,0)) # ajoute fond à fenetre
fenetre.blit(perso, position_perso)
pygame.key.set_repeat(400, 30)
pygame.display.flip() #actualise la fenetre

continuer = 1

while continuer:


    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == pygame.QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                position_perso = position_perso.move(0, 40)
            if event.key == pygame.K_UP:
                position_perso = position_perso.move(0, -40)
            if event.key == pygame.K_LEFT:
                position_perso = position_perso.move(-40, 0)
            if event.key == pygame.K_RIGHT:
                position_perso = position_perso.move(40, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:	#Si clic gauche
                    #On change les coordonnées du perso
                    perso_x = event.pos[0]
                    perso_y = event.pos[1]


    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    pygame.display.flip()
