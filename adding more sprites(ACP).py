import pygame
import random

pygame.init()

# Screen Setup
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Good Looking Collision Game")

clock = pygame.time.Clock()

# --------------------------
# Load Background Image
# --------------------------
background = pygame.image.load("Bg.png")     # use any 700x500 image
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# --------------------------
# Load Player Image
# --------------------------
player_img = pygame.image.load("Player.png")
player_img = pygame.transform.scale(player_img, (50, 50))
player = pygame.Rect(300, 220, 50, 50)

# --------------------------
# Load Enemy Image
# --------------------------
enemy_img = pygame.image.load("Enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (45, 45))

# Create 7 enemies randomly
enemies = []
for i in range(7):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(0, HEIGHT - 50)
    enemies.append(pygame.Rect(x, y, 45, 45))

# Score
score = 0
font = pygame.font.Font(None, 50)

# Animation timer for respawn effect
enemy_flash_time = 0


# ----------------------------------
# Draw glow text for better visuals
# ----------------------------------
def draw_glow_text(text, x, y):
    glow = font.render(text, True, (0, 0, 0))
    screen.blit(glow, (x + 3, y + 3))
    bright = font.render(text, True, (255, 255, 255))
    screen.blit(bright, (x, y))


# Game Loop
running = True
while running:
    screen.blit( background , (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    speed = 5
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.x += speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y < HEIGHT - 50:
        player.y += speed

    # Collision detection
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1

            # Respawn enemy in a random place
            enemy.x = random.randint(0, WIDTH - 50)
            enemy.y = random.randint(0, HEIGHT - 50)

            # Trigger respawn animation
            enemy_flash_time = 10

    # Enemy flash animation
    if enemy_flash_time > 0:
        enemy_flash_time -= 1

    # Draw player
    screen.blit(player_img, player)

    # Draw enemies
    for enemy in enemies:
        if enemy_flash_time > 0:
            # Short bright flash when respawn happens
            flash_img = pygame.transform.scale(enemy_img, (50, 50))
            screen.blit(flash_img, enemy)
        else:
            screen.blit(enemy_img, enemy)

    # Draw Score with glow effect
    draw_glow_text(f"Score : {score}", 20, 20)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
