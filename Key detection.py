import pygame
pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Boundary Detection")
sprite_x = 250
sprite_y = 150
sprite_width = 50
sprite_height = 50
sprite_color = (0, 200, 0)  
speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_x -= speed
    if keys[pygame.K_RIGHT]:
        sprite_x += speed
    if keys[pygame.K_UP]:
        sprite_y -= speed
    if keys[pygame.K_DOWN]:
        sprite_y += speed
    if sprite_x <= 0 or sprite_x + sprite_width >= WIDTH or \
       sprite_y <= 0 or sprite_y + sprite_height >= HEIGHT:
        sprite_color = (200, 0, 0)    
    else:
        sprite_color = (0, 200, 0) 
    screen.fill((20, 20, 40))
    pygame.draw.rect(screen, sprite_color, (sprite_x, sprite_y, sprite_width, sprite_height))
    pygame.display.flip()
pygame.quit()