import pygame   # impordime pygame mooduli
import sys      # impordime süsteemimooduli

pygame.init()   # initsialiseerime Pygame'i

# Akna suurus
screen_size = (300, 300)  # määrame tehtava akna suuruse - 300 x 300 pixlit

# Ekraani loomine
screen = pygame.display.set_mode(screen_size)   # loome Pygame mooduli abil akna, millele on eelnevalt määratud ka suurus 
pygame.display.set_caption("Lumemees - Jaanika Haki")   # määrame Pygame aknale nimetuse


# Peamine mängutsükkel
running = True  # muutuja running loomine
while running:  # algab lõpmatu tsükkel, mis kestab kuni running = True
    for event in pygame.event.get():   # tsükkel mis käib läbi kõik kasutaja poolsed sündmused (nt akna sulgemise)
        if event.type == pygame.QUIT:  # kui kasutaja sulgeb Pygame abil loodud akna...
            running = False    # siis Pygame katkestab akna tsükli

    # Ekraani värv
    screen.fill((0, 0, 0))  # määrab akna taustavärvi - must; rgb kood

    # Ringid (täidetud)
    pygame.draw.circle(screen, [255, 255, 255], [150, 75], 30)   # määrab lumememme 'pea' värvi (valge), asukoha ja suuruse
    pygame.draw.circle(screen, [255, 255, 255], [150, 140], 40)  # määrab lumememme 'keskosa' värvi (valge), asukoha ja suuruse
    pygame.draw.circle(screen, [255, 255, 255], [150, 225], 50)  # määrab lumememme 'alumise osa' värvi (valge), asukoha ja suuruse
    
    # silmad
    pygame.draw.circle(screen, [0, 0, 0], [140, 70], 5)   # annab lumememmele parema silma, musta, 5 pixlit suure
    pygame.draw.circle(screen, [0, 0, 0], [160, 70], 5)   # annab lumememmele vasaku silma, musta, 5 pixlit suure
    
    # ninnu
    pygame.draw.polygon(screen, [255, 0, 0], [[150, 95], [145, 80], [155, 80]])  # nina, punane värv, alumine tipp, vasak tipp, parem tipp
        

    # Ekraani värskendamine
    pygame.display.flip()

# Pygame sulgemine (kui kasutaja on akna sulgenud) ja ressurside kasutamise lõpetamine
pygame.quit()
sys.exit()
