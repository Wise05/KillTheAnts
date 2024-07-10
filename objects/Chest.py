import pygame
from objects import SpriteObject

class Chest(SpriteObject.SpriteObject):
    def __init__(self, x, y, item):
        super().__init__()

        self.closedImage = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\Chest.png")
        self.openImage = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\OpenedChest.png")
        self.currentImage = self.closedImage
        self.hitbox = self.closedImage.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self. item = item
        

    def getSprite(self):
        return self.currentImage

    def getHitbox(self):
        return self.hitbox
    
    def interact(self):
        if self.currentImage != self.openImage:
            self.currentImage = self.openImage
            self.hitbox.y -= 13
            #make item appear and whatever