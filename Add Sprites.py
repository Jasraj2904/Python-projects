import pygame

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Detection with Color Change")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 150, 255)
RED = (255, 80, 80)
BG_NORMAL = WHITE
BG_COLLIDE = (200, 230, 255)

# Sprite Rectangles
player = pygame.Rect(100, 150, 50, 50)
enemy = pygame.Rect(350, 150, 80, 80)

speed = 5

def touching_boundary(rect):
    """Return True if the rectangle touches any screen boundary."""
    return (
        rect.left <= 0 or
        rect.right >= WIDTH or
        rect.top <= 0 or
        rect.bottom >= HEIGHT
    )

running = True
while running:
    # Default background
    background_color = BG_NORMAL
    player_color = BLUE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Movement
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed

    # Stay inside screen but detect collision
    collided = touching_boundary(player)

    if collided:
        player_color = (255, 0, 0)      # Change player color (red)
        background_color = BG_COLLIDE   # Change background

    # Clamp positions AFTER detection
    player.x = max(0, min(WIDTH - player.width, player.x))
    player.y = max(0, min(HEIGHT - player.height, player.y))

    # Draw everything
    screen.fill(background_color)
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, RED, enemy)

    pygame.display.update()
    clock.tick(60)

pygame.quit()