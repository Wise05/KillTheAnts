import pygame
import objects
import objects.player

pygame.init()
pygame.mixer.init()

displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("Kill the Ants!")

player = objects.player.Player()

player.hitbox.x = 20
player.hitbox.y = 20

clock = pygame.time.Clock()
running = True
frames = 0
index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    frames += 1
    if frames == 60:
        frames = 0

    screen.fill((255,255,255))
    print(index)
    screen.blit(player.getWalkPic(index), player.getHitbox())
    if frames % 6 == 0:
        index = (index + 1) % player.getNumOfWalkPics()

    pygame.display.flip()

pygame.quit
