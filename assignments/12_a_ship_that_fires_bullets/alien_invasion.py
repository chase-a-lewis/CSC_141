import sys

import pygame
from ship import Ship
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200, 800))
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Update the background color.
            self.screen.fill((0, 0, 255))
            self.ship.blitme()
            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

pygame.init()

ship = Ship(ai)

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Sideways Shooter")

moving_up = False
moving_down = False

bullets = []
bullet_speed = 7

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True
            elif event.key == pygame.K_SPACE:
                new_bullet = pygame.Rect(
                    ship.right, ship.centery - 3, 15, 6
                )
                bullets.append(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    if moving_up and ship.top > 0:
        ship.y -= 5

    if moving_down and ship.bottom < screen.get_height():
        ship.y += 5

    for bullet in bullets:
        bullet.x += bullet_speed

    for bullet in bullets[:]:
        if bullet.left > screen.get_width():
            bullets.remove(bullet)

    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    pygame.display.flip()
    clock.tick(60)