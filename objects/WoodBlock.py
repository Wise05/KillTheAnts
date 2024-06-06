import pygame
from objects import SpriteObject

class WoodBlock(SpriteObject.SpriteObject):
    def __init__(self, x, y):
        super().__init__()

        self.image = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\WoodBlock2.png")
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def getSprite(self):
        return self.image

    def getHitbox(self):
        return self.hitbox
        
