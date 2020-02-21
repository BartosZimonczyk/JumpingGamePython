import pygame
from horse import Horse
import random
from obstacle import Obstacle
import intervals as i


class Game:
    def __init__(self):
        self.width = 1400
        self.height = 800
        self.game_display = None
        self.background = (255, 230, 220)
        self.ground = 7*self.height/8
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.font_size = 20
        self.font = None
        self.points = 0
        self.g = 0.96
        self.player = Horse(self)
        self.obstacles = list()
        self.time_obs = 0
        self.time = 0

    def draw_obj(self, obj):
        self.game_display.blit(obj.img, (obj.x, obj.y))
        rect = obj.img.get_rect()
        rect.topleft = (obj.x, obj.y)
        pygame.draw.rect(self.game_display, (0, 0, 0), rect, 2)

    def draw_menu(self):
        num_obs = len([ob for ob in self.obstacles])
        obs = self.font.render('Obstacles: {}'.format(num_obs), True, (0, 0, 0))
        rect = obs.get_rect()
        rect.topleft = (0, 0)
        self.game_display.blit(obs, rect)
        obs = self.font.render('Points: {}'.format(self.time/10), True, (0, 0, 0))
        rect = obs.get_rect()
        rect.topleft = (0, self.font_size)
        self.game_display.blit(obs, rect)

    def start_game(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font('TypewriterScribbled.ttf', self.font_size)
        quit_game = False

        while not quit_game:
            self.time += 1
            self.game_display.fill(self.background)
            pygame.draw.line(self.game_display, (0, 0, 0), (0, self.ground), (self.width, self.ground), 10)
            self.draw_menu()
            self.draw_obj(self.player)
            self.player.move()
            self.time_obs += 1 if self.time_obs > 0 else 0
            self.time_obs = 0 if self.time_obs == 40 else self.time_obs
            if random.random() < 0.008 and self.time_obs == 0:
                self.obstacles.append(Obstacle(self))
                self.time_obs += 1
            self.obstacles = [ob for ob in self.obstacles if ob.x > -110 and not ob.remove]
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.player.crouch()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        self.player.jump()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_DOWN:
                        self.player.erect()
                if event.type == pygame.QUIT:
                    quit_game = True
                    pygame.quit()
                    quit()
            pygame.display.flip()
            for ob in self.obstacles:
                self.draw_obj(ob)
                ob.move()
                if i.closed(ob.x, ob.x + ob.width).overlaps(i.closed(self.player.x, self.player.x + self.player.width)) \
                        and i.closed(ob.y, ob.y + ob.height).overlaps(
                        i.closed(self.player.y, self.player.y + self.player.height)):
                    quit_game = True
                    pygame.quit()
                    quit()
            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    g = Game()
    g.start_game()
