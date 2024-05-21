import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idlePlayerPic = r"C:\Users\zevan\Kill The Ants!\images\GregTheSolver.png"
        self.walkingPlayerPics = [
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftFirstStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftSecondStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftHalfwayStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftFirstStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightLegFirstTrans.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightLegSecondTrans.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightHalfwayStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightLegFirstTrans.png"
        ]
        self.idlePlayerPic = pygame.image.load(self.idlePlayerPic).convert_alpha()
        self.idlePlayerPic = pygame.transform.scale(self.idlePlayerPic, (self.idlePlayerPic.get_width() * 2, self.idlePlayerPic.get_height() * 2))
        self.walkImages = [pygame.image.load(pic).convert_alpha() for pic in self.walkingPlayerPics]
        self.hitbox = self.idlePlayerPic.get_rect()
    
    def getWalkPic(self, index):
        return self.walkImages[index]
    
    def getNumOfWalkPics(self):
        return len(self.walkImages)
    
    def getHitbox(self):
        return self.hitbox