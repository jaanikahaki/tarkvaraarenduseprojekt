import pygame
import sys

pygame.init()

# Akna suurus
screen_size = (300, 300)

# Ekraani loomine
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Lumememm - Jaanika Haki")


# Peamine mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekraani värv
    screen.fill((0, 0, 0))

    # Ringid (täidetud)
    pygame.draw.circle(screen, [255, 255, 255], [150, 80], 30)
    pygame.draw.circle(screen, [255, 255, 255], [150, 145], 40)
    pygame.draw.circle(screen, [255, 255, 255], [150, 230], 50)
    
    # silmad
    pygame.draw.circle(screen, [0, 0, 0], [140, 80], 5)
    pygame.draw.circle(screen, [0, 0, 0], [160, 80], 5)
    
    # ninnu
    #pygame.draw.polygon(screen, [255, 51, 0], [150, 80])
        

    # Ekraani värskendamine
    pygame.display.flip()

# Pygame sulgemine
pygame.quit()
sys.exit()


