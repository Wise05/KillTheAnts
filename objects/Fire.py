import pygame
from objects import SpriteObject

class Fire(SpriteObject.SpriteObject):
    def __init__(self, blockOnFire, isOnTop):
        super().__init__()

        self.images = [
            r"C:\Users\zevan\Kill The Ants!\images\Fire1.png",
            r"C:\Users\zevan\Kill The Ants!\images\Fire2.png",
            r"C:\Users\zevan\Kill The Ants!\images\Fire3.png"
        ]
        self.images = [self.loadSprite(img) for img in self.images]
        self.image = self.images[0]
        self.hitbox = self.image.get_rect()
        self.isOnTop = isOnTop

        self.hitbox.x = blockOnFire.getHitbox().x
        self.hitbox.y = blockOnFire.getHitbox().y
        if (isOnTop):
            self.hitbox.y -= 33

        blockOnFire.setFire(self)

        self.frameCounter = 0
        self.imageIndex = 0

    def getSprite(self):
        self.frameCounter += 1
        if self.frameCounter >= 12:
            self.imageIndex = (self.imageIndex + 1) % len(self.images)
            self.image = self.images[self.imageIndex]
            self.frameCounter = 0

        return self.image

    def getHitbox(self):
        return self.hitbox
    
    def getIsOnTop(self):
        return self.isOnTop
    
    def fireSpread(self, block, blocks, fires):
        leftBlock = block.findBlockLeft(blocks)
        rightBlock = block.findBlockRight(blocks)
        upBlock = block.findBlockUp(blocks)
        downBlock = block.findBlockDown(blocks)

        if leftBlock != None and leftBlock.getFire() == None:
            fires.append(Fire(leftBlock, False))
        if rightBlock != None and rightBlock.getFire() == None:
            fires.append(Fire(rightBlock, False))
        if upBlock != None and upBlock.getFire() == None:
            fires.append(Fire(upBlock, False))
        if downBlock != None and downBlock.getFire() == None:
            fires.append(Fire(downBlock, False))
    
    def findFire(self, findMe, fires):
        for fire in fires:
            if fire.getHitbox() == findMe.getHitbox():
                return fire
        return None
        