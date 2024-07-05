from objects import SpriteObject

class Ladder(SpriteObject.SpriteObject):
    def __init__(self, x, y):
        super().__init__()
        #image is 33x33 pixel
        self.image = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\Ladder.png")
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y


    def getSprite(self):
        return self.image

    def getHitbox(self):
        return self.hitbox
    
    def checkLadders(self, player, ladders):
        for i in ladders: 
            if player.getHitbox().colliderect(i.getHitbox()):
                return True
        return False
    