import pygame
import random

# ------------------------------------------------------------------------------
# INITIAL SETUP
# ------------------------------------------------------------------------------

pygame.init()

WIDTH, HEIGHT = 600, 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Moving Sprite to WIN!")

clock = pygame.time.Clock()
FPS = 60

# ------------------------------------------------------------------------------
# HELPER FUNCTION
# ------------------------------------------------------------------------------

def random_color():
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))


# ------------------------------------------------------------------------------
# SPRITE CLASS
# ------------------------------------------------------------------------------

class BoxSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.color = random_color()
        self.image.fill(self.color)

    def move(self, dx=0, dy=0):
        self.rect.x += dx
        self.rect.y += dy

        # Boundary lock
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > HEIGHT: self.rect.bottom = HEIGHT


# ------------------------------------------------------------------------------
# CREATE PLAYER + ENEMY
# ------------------------------------------------------------------------------

player = BoxSprite(150, HEIGHT // 2, 90, 90, random_color())
enemy = BoxSprite(450, HEIGHT // 2, 90, 90, random_color())

# Enemy automatic movement speed
enemy_dx = 3
enemy_dy = 3

all_sprites = pygame.sprite.Group(player, enemy)

# ------------------------------------------------------------------------------
# CUSTOM COLOR EVENT
# ------------------------------------------------------------------------------
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)

# ------------------------------------------------------------------------------
# GAME STATE
# ------------------------------------------------------------------------------
background_color = (25, 25, 25)
has_won = False


# ------------------------------------------------------------------------------
# GAME LOOP
# ------------------------------------------------------------------------------

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not has_won:
            if event.type == CHANGE_COLOR_EVENT:
                player.change_color()
                enemy.change_color()

    # --------------------------------------------------------------------------
    # IF WON → SHOW VICTORY SCREEN ONLY
    # --------------------------------------------------------------------------
    if has_won:
        screen.fill((0, 0, 0))

        font = pygame.font.Font(None, 80)
        text = font.render("YOU WIN!", True, (255, 255, 0))
        screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))

        pygame.display.flip()
        continue

    # --------------------------------------------------------------------------
    # PLAYER MOVEMENT
    # --------------------------------------------------------------------------
    keys = pygame.key.get_pressed()
    speed = 4

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.move(dx=-speed)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.move(dx=speed)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.move(dy=-speed)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.move(dy=speed)

    # --------------------------------------------------------------------------
    # ENEMY AUTOMATIC MOVEMENT
    # --------------------------------------------------------------------------
    enemy.rect.x += enemy_dx
    enemy.rect.y += enemy_dy

    # Bounce on walls
    if enemy.rect.left <= 0 or enemy.rect.right >= WIDTH:
        enemy_dx *= -1
    if enemy.rect.top <= 0 or enemy.rect.bottom >= HEIGHT:
        enemy_dy *= -1

    # --------------------------------------------------------------------------
    # COLLISION → WIN
    # --------------------------------------------------------------------------
    if pygame.sprite.collide_rect(player, enemy):
        has_won = True
        background_color = random_color()
        player.change_color()
        enemy.change_color()

    # --------------------------------------------------------------------------
    # DRAWING
    # --------------------------------------------------------------------------
    screen.fill(background_color)

    # Optional grid background
    for x in range(0, WIDTH, 30):
        pygame.draw.line(screen, (40, 40, 40), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 30):
        pygame.draw.line(screen, (40, 40, 40), (0, y), (WIDTH, y))

    all_sprites.draw(screen)

    font = pygame.font.Font(None, 28)
    msg = font.render("Catch the moving enemy to WIN!", True, (230, 230, 230))
    screen.blit(msg, (20, 20))

    pygame.display.flip()

pygame.quit()