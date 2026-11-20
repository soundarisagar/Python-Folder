import pygame

# Initialize pygame
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Game")

# Set colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create two rectangular sprites
player = pygame.Rect(100, 100, 50, 50)
enemy = pygame.Rect(400, 300, 50, 50)

# Set speed
speed = 1

# Game loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keyboard controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player.y -= speed

    if keys[pygame.K_DOWN]:
        player.y += speed

    if keys[pygame.K_LEFT]:
        player.x -= speed

    if keys[pygame.K_RIGHT]:
        player.x += speed

    # Fill screen with white colour
    screen.fill(WHITE)

    # Draw the two rectangular sprites
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)

    # Update the display
    pygame.display.update()

# Quit pygame
pygame.quit()