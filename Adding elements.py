import pygame
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My First Game Screen")
font = pygame.font.Font(None, 36)
text = font.render("Hello Gamer!", True, (255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 30))
    pygame.draw.rect(screen, (200, 30, 30), (150, 150, 200, 100)) 
    screen.blit(text, (160, 100))
    pygame.display.flip()
pygame.quit()