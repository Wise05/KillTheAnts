import pygame
from objects import SpriteObject

class Ladder(SpriteObject.SpriteObject):
    def __init__(self, x, y):
        super().__init__()
        self.ladderImage = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\Ladder.png")
        self.hitbox = self.ladderImage.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

    def getSprite(self):
        return self.ladderImage

    def getHitbox(self):
        return self.hitbox