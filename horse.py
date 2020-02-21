import pygame
import math


class Horse:
    def __init__(self, game):
        self.game = game
        self.width = 100
        self.height = 200
        self.x = self.width/2
        self.ground = self.game.ground - self.height
        self.y = self.game.ground - self.height
        self.velocity = 0
        self.g = game.g
        self.img = pygame.image.load('horse.png')
        self.img = pygame.transform.flip(self.img, 1, 0)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def move(self):
        self.y -= self.velocity
        self.velocity -= self.g
        if self.y >= self.ground:
            self.velocity = 0
            self.y = self.ground

    def jump(self):
        if self.y == self.ground:
            self.velocity = 20

    def crouch(self):
        self.height = 100
        self.ground = self.game.ground - self.height
        self.y = self.game.ground - self.height
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

    def erect(self):
        self.height = 200
        self.ground = self.game.ground - self.height
        self.y = self.game.ground - self.height
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
