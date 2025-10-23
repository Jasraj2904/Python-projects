import pygame

# Initialize pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600

# Create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My First Game Screen")

# Define colors (RGB format)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw a blue rectangle at the center
    pygame.draw.rect(screen, BLUE, (350, 250, 100, 100))

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
