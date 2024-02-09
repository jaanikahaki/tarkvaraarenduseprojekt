import pygame  # impordime pygame mooduli
import sys     # impordime süsteemimooduli

def draw_grid(screen, grid_size, rows, columns, line_color): # Arvuta ruudu laius ja kõrgus...
    square_width = screen.get_width() // columns  # jagades ekraani laiuse ja 
    square_height = screen.get_height() // rows  # kõrguse

    for row in range(rows):  # ridade tsükkel
        for col in range(columns):  # tulpade/veergude tsükkel
            x = col * square_width  # see tagab, et iga järgmine ruut oleks eelmisest ruudust paremal pool
            y = row * square_height  # see tagab, et iga järgmine ruut on oleks eelmisest ruudust allpool
            pygame.draw.rect(screen, line_color, (x, y, square_width, square_height), 1)  # Pygame joonistagu objektile "ekraan" ruut

# Initsialiseerime Pygame'i
pygame.init()

# Akna suurus ja loomine
screen_size = (640, 480)   # määrame tehtava akna suuruse - 640 x 480 pixlit
screen = pygame.display.set_mode(screen_size)  # loome Pygame mooduli abil akna, millele on eelnevalt määratud ka suurus
pygame.display.set_caption("Ülesanne 3")  # määrame Pygame aknale nimeks "2" (Juhend: Lisa mängu nimeks ülesande number)

# Määratle muutujad
grid_size = 20  # ruudu(stiku) suurus pixlites (ekraani laius 640 pixlit jagatud 32'ga annab 24 rida ja ühe ruudu suuruseks 20p, ehk ekraan on võrdselt ruutudeks jagatud)
rows = 24  # ridade arv
columns = 32  # tulpade/veergude arv
line_color = (214, 25, 12)  # joone värv (RGB kood, vastab ülesandes olevale toonile). Värve saad valida nt - https://www.w3schools.com/colors/colors_picker.asp
screen.fill((154, 255, 153))  # taustavärv (RGB kood, vastab ülesandes olevale toonile). Värve saad valida nt - https://www.w3schools.com/colors/colors_picker.asp

# Mängutsükkel
running = True  # muutuja running loomine
while running:  # algab lõpmatu tsükkel, mis kestab kuni running = True
    for event in pygame.event.get():  # tsükkel mis käib läbi kõik kasutaja poolsed sündmused (nt akna sulgemise)
        if event.type == pygame.QUIT:  # kui kasutaja sulgeb Pygame abil loodud akna...
            running = False  # siis Pygame katkestab akna tsükli

    # Joonistab ruudustiku, kasutades funktsiooni (muutujad on määratletud ridadel 23-26)
    draw_grid(screen, grid_size, rows, columns, line_color)

    # Ekraani värskendamine, tagab sujuva töö
    pygame.display.flip()

# Mängu lõpp (kui kasutaja on akna X'st sulgenud) ja ressurside kasutamise lõpetamine
pygame.quit()
sys.exit()
