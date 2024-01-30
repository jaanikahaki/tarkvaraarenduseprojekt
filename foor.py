import pygame   # impordime pygame mooduli
import sys      # impordime süsteemimooduli

pygame.init()   # initsialiseerime Pygame'i

# Akna suurus
screen_size = (300, 300)    # määrame tehtava akna suuruse - 300 x 300 pixlit

# Ekraani loomine
screen = pygame.display.set_mode(screen_size)   # loome Pygame mooduli abil akna, millele on eelnevalt määratud ka suurus
pygame.display.set_caption("Foor - Jaanika Haki")  # määrame Pygame aknale nimetuse


# Peamine mängutsükkel
running = True    # muutuja running loomine
while running:    # algab lõpmatu tsükkel, mis kestab kuni running = True
    for event in pygame.event.get():   # 
        if event.type == pygame.QUIT:  # kui kasutaja sulgeb Pygame abil loodud akna...
            running = False   # siis Pygame katkestab akna tsükli

    # Ekraani värv
    screen.fill((0, 0, 0))   # määrab akna taustavärvi - must; rgb kood
    
    # Ristkülik
    pygame.draw.rect(screen, [129, 126, 127], [100, 10, 100, 270], 2) #määrab fooritulesid ümbritseva ristküliku (ainult ümbritsev joon) värvi (hall), suuruse ja asukoha ning joone paksuse (2 pixlit)

    # Ringid (täidetud)
    pygame.draw.circle(screen, [255, 0, 0], [150, 60], 40)  # foori esimene ring (punane, asukoht, suurus)
    pygame.draw.circle(screen, [255, 255, 0], [150, 145], 40)  # foori teine ring (kollane, asukoht, suurus)
    pygame.draw.circle(screen, [0, 255, 0], [150, 230], 40)   # foori esimene ring (roheline, asukoht, suurus)

    # Ekraani värskendamine
    pygame.display.flip()  # Pygame ekraanivärskenduse funktsioon, mis toob nähtavale kõik eelnevalt loodud graafilised lahendused (foori)

# Pygame sulgemine
pygame.quit() # lõpetab Pygame mooduli toimimise selle akna jaoks, kui aken on suletud, et vabastada arvuti ressursid
sys.exit()    # lõpetab süsteemimooduli toimimise selle...
