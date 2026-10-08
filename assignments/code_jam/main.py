import pygame

pygame.init()

# Create the game window
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("My God of War Inspired Game")

# Game clock
clock = pygame.time.Clock()

# Player
player = pygame.Rect(100, 500, 50, 100)

# Player settings
player_speed = 5
gravity = 1
jump_strength = -18
velocity_y = 0

# Game loop
running = True

while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard input
    keys = pygame.key.get_pressed()

    # Move left
    if keys[pygame.K_a]:
        player.x -= player_speed

    # Move right
    if keys[pygame.K_d]:
        player.x += player_speed

    # Jump with W
    if keys[pygame.K_w] and player.bottom >= 600:
        velocity_y = jump_strength

    # Gravity
    velocity_y += gravity
    player.y += velocity_y

    # Keep player on the ground
    if player.bottom >= 600:
        player.bottom = 600
        velocity_y = 0

    # Crouch with S
    if keys[pygame.K_s]:
        player.height = 60
    else:
        player.height = 100

    # Keep feet in the same position
    player.bottom = 600

    # Draw background
    screen.fill((30, 30, 30))

    # Draw player
    pygame.draw.rect(screen, (200, 50, 50), player)

    # Update screen
    pygame.display.flip()

    # Run at 60 FPS
    clock.tick(60)

pygame.quit()