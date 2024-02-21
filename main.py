import pygame
import sys


pygame.init()
# ініціалізація mixer
pygame.mixer.init()

# для коротких звуків буде використовуватися Sound
sound1 = pygame.mixer.Sound("sounds/click.wav")
sound2 = pygame.mixer.Sound("sounds/coin.wav")
sound3 = pygame.mixer.Sound("sounds/win.wav")
sound4 = pygame.mixer.Sound("sounds/flapping.wav")
w, h = 800, 600

screen = pygame.display.set_mode((w, h))


run = True

# для довгих звуків\фонової музики
pygame.mixer.music.set_volume(0.1)

pygame.mixer.music.load("sounds/blue_dot_session.wav")

# аби відтворити таку композицію
pygame.mixer.music.play(-1)   # в дужках передаємо кількість повторів
# аби пісня відтворювалася поки програма запущена, передаємо в дужки -1

quit_img = pygame.image.load("qit.png")
quit_img = pygame.transform.scale(quit_img, (150, 50))
# отримуємо прямокутник зображення
quit_rect = quit_img.get_rect()
# розміщуємо зображення по центру
quit_rect.center = (400, 300)

BLACK = (0, 0, 0)
button_rect = pygame.Rect(300, 250, 200, 100)# x, y, width, height

# пауза - pause
# зняти з паузи - unpause
# зупинити відтворення - stop
# відтворити - play

# play не дуже підходить для того, аби зняти  якесь відтворення з паузи, тому що починатиме відтворювати все спочатку
# unpause - відтворює звук із того моменту, на якому він був зупинений

# встановлюємо гучність лише для звуків у грі
sound2.set_volume(0.1) # можна записати значення від 0.0 до 1.0
sound3.set_volume(0.1)
sound4.set_volume(0.1)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if quit_rect.collidepoint(event.pos):
                sound3.play(2)
                pygame.mixer.music.pause()
                pygame.time.delay(2000)
                pygame.mixer.music.unpause()
                # run = False


    
    screen.fill((0, 0, 200))
    pygame.draw.rect(screen, BLACK, button_rect)
    screen.blit(quit_img, quit_rect)
    pygame.display.update()



pygame.quit()
sys.exit()


"""

import pygame
import sys


pygame.init()
# ініціалізація mixer
pygame.mixer.init()

# для коротких звуків буде використовуватися Sound
sound1 = pygame.mixer.Sound("sounds/click.wav")
sound2 = pygame.mixer.Sound("sounds/coin.wav")
sound3 = pygame.mixer.Sound("sounds/win.wav")
sound4 = pygame.mixer.Sound("sounds/flapping.wav")
w, h = 800, 600

screen = pygame.display.set_mode((w, h))


run = True

# для довгих звуків\фонової музики
pygame.mixer.music.set_volume(0.1)

pygame.mixer.music.load("sounds/blue_dot_session.wav")

# аби відтворити таку композицію
pygame.mixer.music.play(-1)   # в дужках передаємо кількість повторів
# аби пісня відтворювалася поки програма запущена, передаємо в дужки -1

quit_img = pygame.image.load("qit.png")
# отримуємо прямокутник зображення
quit_rect = quit_img.get_rect()
# розміщуємо зображення по центру
quit_rect.center = (400, 300)


# встановлюємо гучність лише для звуків у грі
sound2.set_volume(0.1) # можна записати значення від 0.0 до 1.0
sound3.set_volume(0.1)
sound4.set_volume(0.1)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        sound1.play()
    if keys[pygame.K_w]:
        sound2.play()
    if keys[pygame.K_q]:
        sound3.play()
    if keys[pygame.K_a]:
        sound4.play()

pygame.quit()
sys.exit()

# безкоштовна музика, яка не потребує ліцензії - https://mixkit.co/free-sound-effects/game-over/
# генеруємо зображення(текст з різними шрифтами) - https://gdcolon.com/gdfont

"""