import pygame
import objects
import objects.Player
import objects.Ladder

pygame.init()
pygame.mixer.init()

displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("Kill the Ants!")

player = objects.Player.Player(40, 500)


ladders = [objects.Ladder.Ladder(0,560), objects.Ladder.Ladder(0,520), objects.Ladder.Ladder(0,480)]

def checkLadders():
    for i in ladders: 
        if player.getHitbox().colliderect(i.getHitbox()):
            return True
    return False

clock = pygame.time.Clock()
running = True
frames = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    frames += 1
    if frames == 60:
        frames = 0

    player.setTouchesLadder(checkLadders())
    player.movement()

    screen.fill((255,255,255))
    for i in ladders: screen.blit(i.getSprite(), i.getHitbox())
    screen.blit(player.getPlayerSprite(), player.getHitbox())

    pygame.display.flip()

pygame.quit
