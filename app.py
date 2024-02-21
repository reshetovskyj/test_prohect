import pygame
import sys
from pygame.constants import (QUIT, K_LEFT, K_RIGHT, K_UP, K_DOWN, 
                              K_w, K_a, K_s, K_d, K_SPACE)

pygame.init()


# оголошуємо клас для персонажа
class Character:
    """Клас, який описує структуру базового персонажа"""
    def __init__(self, x, y, image_path) -> None:
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(pygame.image.load(image_path),
                                            (80, 80))
        self.speed = 5

    def draw(self, screen):
        """Метод, який відповідає за відмальовку на екрані"""
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction):
        """Метод, що відповідає за рух персонажа"""
        if direction == "UP":
            self.y -= self.speed
        elif direction == "DOWN":
            self.y += self.speed
        elif direction == "LEFT":
            self.x -= self.speed 
        elif direction == "RIGHT":
            self.x += self.speed 

# оголосити клас, який буде успадкований від стандартного класу персонажа
class Mage(Character):
    def __init__(self, x, y, speed, image_path):
        super().__init__(x, y, image_path)
        self.speed = speed
        self.fire = pygame.transform.scale(pygame.image.load("ball_36.png"), (30, 30))
        self.fire_x = x
        self.fire_y = y
        self.is_attacking = False

    def attack(self):
        self.is_attacking = True
        self.fire_x = self.x
        self.fire_y = self.y

        
        

w = 1000
h = 800

screen = pygame.display.set_mode((w, h))

# створюємо одного персонажа
player = Character(900, 100, "icon_303.png")
# створюємо іншого пересонажа на основі одного класу
mag = Mage(100, 100, 10, "icon_457.png")


running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        player.move("RIGHT")
    if keys[K_LEFT]:
        player.move("LEFT")
    if keys[K_DOWN]:
        player.move("DOWN")
    if keys[K_UP]:
        player.move("UP")

    if keys[K_d]:
        mag.move("RIGHT")
    if keys[K_a]:
        mag.move("LEFT")
    if keys[K_s]:
        mag.move("DOWN")
    if keys[K_w]:
        mag.move("UP")
 
    if keys[K_SPACE]:
        mag.attack()

    if mag.is_attacking:
        mag.fire_x += 25
        if mag.fire_x > w:
            mag.is_attacking = False

    screen.fill((34, 210, 255))
    # малювання персонажа
    player.draw(screen)
    mag.draw(screen)

    if mag.is_attacking:
        screen.blit(mag.fire, (mag.fire_x, mag.fire_y))

    # оновлення дисплею
    pygame.display.update()

    # контроль швидоксті оновлення
    pygame.time.Clock().tick(60)






