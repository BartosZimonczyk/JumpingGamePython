import pygame
import random


class Obstacle:
    def __init__(self, game):
        self.game = game
        self.width = random.randint(30, 60)
        self.height = random.randint(self.width, 100)
        self.x = game.width + 130
        self.y = random.choice((game.ground - self.height, game.ground - self.height - 150))
        self.velocity = 8
        self.img = pygame.image.load('obs.png')
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.remove = False

    def move(self):
        self.x -= self.velocity
