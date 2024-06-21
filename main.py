import pygame
import objects
import objects.Player
import objects.Ladder
import objects.WoodBlock
import objects.Fire

pygame.init()
pygame.mixer.init()

#grid is 25x19 block units
#block units are 33x33 pixels
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("Kill the Ants!")

player = objects.Player.Player(200, 500)

blocks = [objects.WoodBlock.WoodBlock(33, 600 - 33*5), objects.WoodBlock.WoodBlock(33 * 2, 600 - 33*5), objects.WoodBlock.WoodBlock(33*3, 600 - 33*4)]
ladders = [objects.Ladder.Ladder(0,600-33), objects.Ladder.Ladder(0,600-66), objects.Ladder.Ladder(0,600-99), objects.Ladder.Ladder(0, 600 - (33 * 4)), objects.Ladder.Ladder(0, 600 - (33 * 5))]
fire = [objects.Fire.Fire(0,0)]


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

    if ladders != None:
        player.setTouchesLadder(ladders[0].checkLadders(player, ladders))
    player.touchingblock(blocks)
    player.movement()

    screen.fill((220,190,140))
    for i in ladders: screen.blit(i.getSprite(), i.getHitbox())
    for i in blocks: screen.blit(i.getSprite(), i.getHitbox())
    for i in fire: screen.blit(i.getSprite(), i.getHitbox())
    screen.blit(player.getPlayerSprite(), player.getHitbox())

    pygame.display.flip()

pygame.quit
