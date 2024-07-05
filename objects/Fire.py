import pygame
from objects import SpriteObject
import random
import objects
import objects.StoneBlock

class Fire(SpriteObject.SpriteObject):
    def __init__(self, blockOnFire):
        super().__init__()

        self.images = [
            r"C:\Users\zevan\Kill The Ants!\images\Fire1.png",
            r"C:\Users\zevan\Kill The Ants!\images\Fire2.png",
            r"C:\Users\zevan\Kill The Ants!\images\Fire3.png"
        ]
        self.images = [self.loadSprite(img) for img in self.images]
        self.image = self.images[0]
        self.hitbox = self.image.get_rect()

        self.hitbox.x = blockOnFire.getHitbox().x
        self.hitbox.y = blockOnFire.getHitbox().y

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

        self.chanceSpread(block, leftBlock, blocks, fires)
        self.chanceSpread(block, rightBlock, blocks, fires)
        self.chanceSpread(block, upBlock, blocks, fires)
        self.chanceSpread(block, downBlock, blocks, fires)
    
    def findFire(self, findMe, fires):
        for fire in fires:
            if fire.getHitbox() == findMe.getHitbox():
                return fire
        return None
    
    def chanceSpread(self, burningBlock, spreadBlock, blocks, fires):
        if (random.randint(0, 100) <= 95) and not isinstance(spreadBlock, objects.StoneBlock.StoneBlock):
            if spreadBlock != None and spreadBlock.getFire() == None:
                fires.append(Fire(spreadBlock))
            try: #I feel like I shouldn't do this, but whatever, it works
                blocks.remove(burningBlock)
                fires.remove(burningBlock.getFire().findFire(burningBlock.getFire(), fires))
            except:
                do = "nothing"


        
        