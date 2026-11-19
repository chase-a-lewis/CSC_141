import sys
import pygame
from ship import Ship
from alien import Alien
from bullet import Bullet

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Sideways Shooter")

        self.ship_image = Ship(self).image

        self.ship_image = pygame.transform.scale(self.ship_image, (100, 100))
        self.ship = self.ship_image.get_rect()
        self.ship.left = 50
        self.ship.centery = 400

        self.moving_up = False
        self.moving_down = False
        self.ship_speed = 5

        self.bullet_image = Bullet(self).image
        # Bullet settings
        self.bullets = []
        self.bullet_speed = 10

        self.clock = pygame.time.Clock()

    def run_game(self):

        while True:
            self.check_events()
            self.update_ship()
            self.update_bullets()
            self.update_screen()

    def check_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.moving_up = True

                elif event.key == pygame.K_DOWN:
                    self.moving_down = True

                elif event.key == pygame.K_SPACE:
                    self.fire_bullet()

            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    self.moving_up = False

                elif event.key == pygame.K_DOWN:
                    self.moving_down = False

    def update_ship(self):

        if self.moving_up and self.ship.top > 0:
            self.ship.y -= self.ship_speed

        if self.moving_down and self.ship.bottom < 800:
            self.ship.y += self.ship_speed

    def fire_bullet(self):

        bullet = pygame.Rect(
            self.ship.right,
            self.ship.centery - 3,
            20,
            6
        )

        self.bullets.append(bullet)

    def update_bullets(self):

        for bullet in self.bullets:
            bullet.x += self.bullet_speed

        for bullet in self.bullets[:]:
            if bullet.left > 1200:
                self.bullets.remove(bullet)

    def update_screen(self):

        self.screen.fill((0, 0, 255))

        # Draw Kratos
        self.screen.blit(pygame.transform.scale(self.ship_image, (100, 100)), self.ship)

        # Draw bullets
        for bullet in self.bullets:
            self.screen.blit(pygame.transform.scale(self.bullet_image, (100, 100)), bullet)

        pygame.display.flip()

        self.clock.tick(60)


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
