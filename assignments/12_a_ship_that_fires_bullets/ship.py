import pygame

class Ship:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('assignments/12_a_ship_that_fires_bullets/images/pacman.png')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)