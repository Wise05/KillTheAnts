import pygame
from objects import SpriteObject
import random

class WoodBlock(SpriteObject.SpriteObject):
    def __init__(self, x, y):
        super().__init__()

        self.image = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\WoodBlock2.png")
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.burningTimer = 0
        self.fire = None

    def getSprite(self):
        return self.image

    def getHitbox(self):
        return self.hitbox

    def setFire(self, fire):
        self.fire = fire

    def getFire(self):
        return self.fire

    def burnTick(self, blocks, fires):
        if self.fire != None and not self.fire.getIsOnTop():
            self.burningTimer += 1

            if self.burningTimer >= 100:
                self.fire.fireSpread(self, blocks, fires)
                self.burningTimer = 0
                return self.fire
            
        return None
    
    def findBlockLeft(self, blocks):
        for block in blocks:
            if block.getHitbox().x + 33 == self.getHitbox().x and block.getHitbox().y == self.getHitbox().y:
                return block
        return None
    def findBlockRight(self, blocks):
        for block in blocks:
            if block.getHitbox().x - 33 == self.getHitbox().x and block.getHitbox().y == self.getHitbox().y:
                return block
        return None
    def findBlockUp(self, blocks):
        for block in blocks:
            if block.getHitbox().x == self.getHitbox().x and block.getHitbox().y + 33 == self.getHitbox().y:
                return block
        return None
    def findBlockDown(self, blocks):
        for block in blocks:
            if block.getHitbox().x == self.getHitbox().x and block.getHitbox().y - 33 == self.getHitbox().y:
                return block
        return None
        
