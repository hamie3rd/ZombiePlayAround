import pygame
import random
pygame.init()

clock = pygame.time.Clock()
displayWidth = 800
displayHeight = 600
white_color = (255,255,255)
gravity = 0.3

zombie_img = pygame.image.load('zombie.png')
zombie_width = 80
zombie_height = 80

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))


def zombie(x,y):





exit = False

x = (displayWidth * 0.45)
y = (displayHeight * 0.6)
y_speed = 0
x_speed = 0

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_speed += -7
                x_speed = random.choice([-10,10, 50, -50])



    gameDisplay.fill(white_color)
    y_speed += gravity
    y += y_speed
    x += x_speed
    if x < 0:
        x_speed = abs(x_speed)
    elif x + zombie_width > displayWidth:
        x_speed = (abs(x_speed)) * -1
    if y > displayHeight:
        y_speed = -20

    zombie(x,y)
    pygame.display.update()
    clock.tick(60)