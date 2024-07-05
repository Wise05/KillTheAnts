import objects
import objects.Fire
import objects.WoodBlock
import pygame

pygame.init()
displayWidth = 800
displayHeight = 600
screen = pygame.display.set_mode((displayWidth, displayHeight))

fires = [objects.Fire.Fire(objects.WoodBlock.WoodBlock(33, 600 - 33*5), False)]

print(fires)