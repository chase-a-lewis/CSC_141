import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Rocket")

bg_color = (0, 0, 255)

rocket = pygame.Rect(575, 375, 50, 50)

moving_right = False
moving_left = False
moving_up = False
moving_down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    if moving_right and rocket.right < screen.get_width():
        rocket.x += 5
    if moving_left and rocket.left > 0:
        rocket.x -= 5
    if moving_up and rocket.top > 0:
        rocket.y -= 5
    if moving_down and rocket.bottom < screen.get_height():
        rocket.y += 5

    screen.fill(bg_color)
    pygame.draw.rect(screen, (255, 0, 0), rocket)
    pygame.display.flip()

    clock.tick(60)