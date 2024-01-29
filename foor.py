import pygame
import sys

pygame.init()

# Akna suurus
screen_size = (300, 300)

# Ekraani loomine
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Foor - Jaanika Haki")

# Ristküliku ja ringide suurused ja värvid
rect_size = (100, 275)
rect_color = (140, 140, 140)

# Peamine mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ekraani värv
    screen.fill((0, 0, 0))

    # Ristkülik (vaid ümbritsev joon)
    rect = pygame.Rect((screen_size[0] - rect_size[0]) // 2, (screen_size[1] - rect_size[1]) // 2, *rect_size)
    pygame.draw.rect(screen, rect_color, rect, 1)  # 1 tähendab joone laiust

    # Ringid (täidetud)
    pygame.draw.circle(screen, (255, 0, 0), (150, 60), 40)
    pygame.draw.circle(screen, (255, 255, 0), (150, 145), 40)
    pygame.draw.circle(screen, (0, 255, 0), (150, 230), 40)

    # Ekraani värskendamine
    pygame.display.flip()

# Pygame sulgemine
pygame.quit()
sys.exit()
