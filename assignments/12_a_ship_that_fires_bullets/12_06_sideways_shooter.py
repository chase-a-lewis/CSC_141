import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Sideways Shooter")

bg_color = (230, 230, 230)

ship = pygame.Rect(50, 375, 60, 50)

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

    screen.fill(bg_color)

    pygame.draw.rect(screen, (255, 0, 0), ship)

    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    pygame.display.flip()
    clock.tick(60)