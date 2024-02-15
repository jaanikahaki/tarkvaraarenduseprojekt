#Loo mäng 640×480 suurusega
# Lisa taustapilt
# Lisa ekraani alla keskele punane auto
# Lisa siniste autode animatsioon ülevalt alla
# - autod jäävad tee vahemikku
# - alustavad erinevatelt kõrgustelt
# - kui auto alla jõuab, hakkab ta uuesti ülevalt alla liikuma
# Kuva skoor
# - kui sinine auto jõuab alla, lisatakse skoorile punkte juurde
# - arv, mida soovid lisada tekstikasti, tuleb teisendada tekstiks str(number)

import pygame  # impordime pygame mooduli
import sys     # impordime süsteemimooduli
import random  # impordime Python'i "random" mooduli

pygame.init()  # initsialiseeri Pygame

# ekraani seadistamine
screenX = 640  # X telje pikkus pixlites
screenY = 480  # Y telje pikkus pixlites
screen = pygame.display.set_mode([screenX, screenY])  # loome Pygame mooduli abil akna, millele on eelnevalt määratud ka suurus
pygame.display.set_caption("Haki ralli animatsioon")  # akna nimetuse määramine
clock = pygame.time.Clock() # 'kaadrit sekundis' ehk fps kontrollimine clock rakenduse abil

# pildifailid
taust = pygame.image.load('bg_rally.jpg')  # taust
punane_auto = pygame.image.load('f1_red.png')  # punane f1 auto
sinine_auto = pygame.image.load('f1_blue.png')  # sinine f1 auto

# punase auto positsioon X telje järgi, ekraan kaheks jagatuna (//2), 10 pixlit ekraani alumisest äärest eemal, et mitte liiga alla jääda
pun_auto_pos = [screenX // 2 - punane_auto.get_width() // 2, screenY - punane_auto.get_height() - 10]

# siniste autode random generated positsioonid ja kiirus, 5 autot korraga (for_ in range real), mida saab muuta vastavalt soovile
# X telje keskpunktist vasakule või paremale on 175 pixlit (tee ulatuses)
# sinised autod tulevad suvalise kiirusega vahemikus 2-5 pixlit mängutsükli kohta
sin_autod = [{'pos': [random.randint(screenX // 2 - 175, screenX // 2 + 175 - sinine_auto.get_width()), random.randint(-screenY, 0)],
              'speed': random.randint(2, 5)} for _ in range(5)]

# skoori muutujate määramine
skoor = 0
font = pygame.font.Font(None, 36)

# alljärgnev kontrollib sündmusi ehk kas kasutaja on mängu sulgenud või mitte
m2ng_l2bi = False # kuni animatsioon veel käib (kasutaja pole sulgenud), siis see jätkub
while not m2ng_l2bi:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # kui kasutaja on mängu sulgenud X'ist siis
            pygame.quit() # sulgub pygame
            sys.exit()  # ja süsteemi moodulid

# võimalus liigutada vasaku ja parema nooleklahviga punast autot, et sinised temast üle ei sõidaks
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and pun_auto_pos[0] > screenX // 2 - 175:
#         pun_auto_pos[0] -= 5
#     if keys[pygame.K_RIGHT] and pun_auto_pos[0] < screenX // 2 + 175 - punane_auto.get_width():
#         pun_auto_pos[0] += 5

# siniste autode liikumine grupina ja kiirus, kontrollib kas auto on jõudnud ekraanilt "välja", et ta siis uuesti jooksma panna
    for sin_auto in sin_autod:
        sin_auto['pos'][1] += sin_auto['speed']
        if sin_auto['pos'][1] > screenY:
            # kui sinine auto jõuab alla, alustab ta uuesti ülevalt, iga kord kui alla jõuab, lisatakse skoorile 1 punkt
            sin_auto['pos'] = [random.randint(screenX // 2 - 175, screenX // 2 + 175 - sinine_auto.get_width()), random.randint(-screenY, 0)]
            sin_auto['speed'] = random.randint(2, 5)
            skoor += 1

    # taustapilt
    screen.blit(taust, (0, 0))

    # punane auto
    screen.blit(punane_auto, pun_auto_pos)

    # sinine auto siniste autode grupis
    for sin_auto in sin_autod:
        screen.blit(sinine_auto, sin_auto['pos'])

    # skoori kuvamine üleval vasakus nurgas, valge tekst
    skoor_text = font.render(f"Skoor: {skoor}", True, (255, 255, 255))
    screen.blit(skoor_text, (10, 10))  # teksti koordinaadid
    # ekraani värskendamine, tagab sujuva töö
    pygame.display.flip()
    clock.tick(30)  # kaadrid per sekund piiramine 30-ni