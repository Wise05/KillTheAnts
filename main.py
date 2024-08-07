import pygame
import objects
import objects.Player
import objects.Ladder
import objects.WoodBlock
import objects.Fire
import objects.StoneBlock
import objects.Chest

pygame.init()
pygame.mixer.init()

#grid is 25x19 block units
#block units are 33x33 pixels
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))
caption = pygame.display.set_caption("Kill the Ants!")

player = objects.Player.Player(200, 500)

blocks = [objects.WoodBlock.WoodBlock(33, 600 - 33*5), objects.WoodBlock.WoodBlock(33 * 2, 600 - 33*5), objects.WoodBlock.WoodBlock(33*3, 600 - 33*4), objects.StoneBlock.StoneBlock(33 * 3, 600 - 33*5)]
ladders = [objects.Ladder.Ladder(0,600-33), objects.Ladder.Ladder(0,600-66), objects.Ladder.Ladder(0,600-99), objects.Ladder.Ladder(0, 600 - (33 * 4)), objects.Ladder.Ladder(0, 600 - (33 * 5))]
fires = [objects.Fire.Fire(blocks[0])]
actableObjects = [objects.Chest.Chest(33*10, 600 -33, None)]


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
    player.movement(actableObjects)

    for block in blocks:
        if isinstance(block, objects.WoodBlock.WoodBlock):
            fire = block.burnTick(blocks, fires) 

    screen.fill((60,40,30))
    for i in ladders: screen.blit(i.getSprite(), i.getHitbox())
    for i in blocks: screen.blit(i.getSprite(), i.getHitbox())
    for i in fires: screen.blit(i.getSprite(), i.getHitbox())
    for i in actableObjects: screen.blit(i.getSprite(), i.getHitbox())
    screen.blit(player.getPlayerSprite(), player.getHitbox())

    pygame.display.flip()

pygame.quit
