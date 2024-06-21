import pygame
from objects import SpriteObject

class Fire(SpriteObject.SpriteObject):
    def __init__(self, x, y):
        super().__init__()

        self.images = [
            r"C:\Users\zevan\Kill The Ants!\images\Fire1.png",
            r"C:\Users\zevan\Kill The Ants!\images\Fire2.png",
            r"C:\Users\zevan\Kill The Ants!\images\Fire3.png"
        ]
        self.images = [self.loadSprite(img) for img in self.images]
        self.image = self.images[0]
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
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