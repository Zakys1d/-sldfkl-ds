import pygame
import main
import math
pygame.init()

picture1 = pygame.image.load("background.jpg")
picture2 = pygame.image.load("background2.jpg")

screen = 1

enemy = pygame.Rect(100,100,50,50)


window = pygame.display.set_mode((600,400))
clock = pygame.time.Clock()
player = main.Player((150,150))
game = True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if player.rect.x < 0:
        player.rect.x = 600 - player.rect.width
        screen = 2
    if player.rect.x > 600:
        player.rect.x = 0
        screen = 1

    if player.rect.y < 0:
        player.rect.y = 400 - player.rect.width
    if player.rect.y > 400:
        player.rect.y = 0 

    if screen == 1:
        window.blit(picture1, (0,0))
    elif screen == 2:
        window.blit(picture2, (0,0))

    dx = player.rect.x - enemy.x
    dy = player.rect.y - enemy.y

    dist = math.hypot(dx, dy)

    if dist != 0:
        dx /= dist
        dy /= dist

    enemy.x += dx * 3
    enemy.y += dy * 3
    pygame.draw.rect(window,(255,0,0), enemy)



    player.events(event)
    #window.fill((0,0,0))
    window.blit(player.image, player.rect)

    clock.tick(30)
    pygame.display.update()