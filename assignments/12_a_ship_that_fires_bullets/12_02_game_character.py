import sys
import pygame

class Character:
    """A class to display a game character."""

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("assignments/12_a_ship_that_fires_bullets/images/kratos_idle.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center

    def draw_character(self):
        self.screen.blit(self.image, self.rect)


pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Game Character")

bg_color = (0, 0, 0)

character = Character(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(bg_color)
    character.draw_character()
    pygame.display.flip()