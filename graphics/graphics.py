#! /usr/bin/env python3
# coding: utf-8

import pygame
from config import constants


class Graphics:

    def __init__(self, laby):
        self.laby = laby
        pygame.init()

        # Initialize window
        self.size_image = constants.size_image
        self.width = (self.laby.y+1) * self.size_image
        self.height = (self.laby.x+1) * self.size_image
        self.window = pygame.display.set_mode((0, 0))
        self.icone = pygame.image.load(constants.icone).convert_alpha()
        pygame.display.set_caption(constants.windows_title)
        pygame.display.set_icon(self.icone)

        # Initialize images
        self.banner = pygame.image.load(constants.banner).convert()

        self.background = pygame.image.load(constants.background).convert()
        self.background = pygame.transform.scale(
            self.background,
            (self.size_image, self.size_image))

        self.walls = pygame.image.load(constants.walls).convert()
        self.walls = pygame.transform.scale(
            self.walls,
            (self.size_image, self.size_image))

        self.hero = pygame.image.load(constants.hero).convert_alpha()
        self.hero = pygame.transform.scale(
            self.hero,
            (self.size_image, self.size_image))

        self.guardian = pygame.image.load(constants.guardian).convert_alpha()
        self.guardian = pygame.transform.scale(
            self.guardian,
            (self.size_image, self.size_image))

        self.object0 = pygame.image.load(constants.object0).convert_alpha()
        self.object0 = pygame.transform.scale(
            self.object0,
            (self.size_image, self.size_image))

        self.object1 = pygame.image.load(constants.object1).convert_alpha()
        self.object1 = pygame.transform.scale(
            self.object1,
            (self.size_image, self.size_image))

        self.object2 = pygame.image.load(constants.object2).convert_alpha()
        self.object2 = pygame.transform.scale(
            self.object2,
            (self.size_image, self.size_image))

    def welcome_game(self, welcome, start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
                welcome = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start = False
                    welcome = False
                elif event.key == pygame.K_RETURN:
                    welcome = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                welcome = False

            pygame.display.set_mode(self.banner.get_rect().size)
            self.window.blit(self.banner, (0, 0))
            pygame.display.flip()
        return welcome, start

    def win_game(self, start, create_player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start = False
                elif event.key == pygame.K_RETURN:
                    self.laby.user.end = False
                    create_player = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.laby.user.end = False
                create_player = True
            dark_surface = pygame.Surface(
                (self.width, self.height), pygame.SRCALPHA)

            dark_surface.fill((30, 28, 30, 128))
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("You win!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.width/2, self.height/2))

            self.window.blit(dark_surface, (0, 0))
            self.window.blit(text, text_rect)
            pygame.display.flip()
        return start, create_player

    def lose_game(self, start, create_player):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start = False
                elif event.key == pygame.K_RETURN:
                    self.laby.user.end = False
                    create_player = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.laby.user.end = False
                create_player = True

            dark_surface = pygame.Surface(
                (self.width, self.height), pygame.SRCALPHA)

            dark_surface.fill((30, 28, 30, 128))
            font = pygame.font.SysFont("comicsansms", 72)
            text = font.render("You lose!", True, (255, 255, 255))
            text_rect = text.get_rect(center=(self.width/2, self.height/2))

            self.window.blit(dark_surface, (0, 0))
            self.window.blit(text, text_rect)
            pygame.display.flip()
        return start, create_player

    def play_game(self, start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    start = False
                if event.key == pygame.K_RIGHT:
                    self.laby.user.move("RIGHT")
                if event.key == pygame.K_LEFT:
                    self.laby.user.move("LEFT")
                if event.key == pygame.K_UP:
                    self.laby.user.move("UP")
                if event.key == pygame.K_DOWN:
                    self.laby.user.move("DOWN")
            self.update_views_map()
        return start

    def update_views_map(self):
        pygame.display.set_mode((self.width, (self.height+60)))
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
        text = font.render(
            "Items recovered : " + str(self.laby.user.objects_collect),
            True,
            (255, 255, 255))

        self.window.blit(text, (15, self.height))
        pygame.display.flip()
