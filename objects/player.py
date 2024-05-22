import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # player is 22 x 40 px
        self.idleImageRight = r"C:\Users\zevan\Kill The Ants!\images\GregTheSolver.png"
        self.walkingPlayerPics = [
            r"C:\Users\zevan\Kill The Ants!\images\GregRightLegFirstTrans.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftFirstStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftSecondStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftHalfwayStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregLeftFirstStep.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightLegFirstTrans.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightLegSecondTrans.png",
            r"C:\Users\zevan\Kill The Ants!\images\GregRightHalfwayStep.png"
        ]
        self.idleImageRight = pygame.image.load(self.idleImageRight).convert_alpha()
        self.walkImagesRight = [pygame.image.load(pic).convert_alpha() for pic in self.walkingPlayerPics]
        self.idleImageLeft = pygame.transform.flip(self.idleImageRight, True, False)
        self.walkImagesLeft = [pygame.transform.flip(pic, True, False) for pic in self.walkImagesRight]
        self.hitbox = self.idleImageRight.get_rect()
        self.aniIndex = 0
        self.frameCounter = 0
        self.currentDirection = '>'
        self.currentPlayerImg = self.idleImageRight

        self.xDelta = 0
        self.yDelta = 0
        self.keyPressed = None
    
    def getWalkImageRight(self):
        return self.walkImagesRight[self.aniIndex]

    def getWalkImageLeft(self):
        return self.walkImagesLeft[self.aniIndex]
    
    def getPlayerSprite(self):
        return self.currentPlayerImg
    
    def updateWalkAnimationIndex(self):
        self.aniIndex = (self.aniIndex + 1) % len(self.walkImagesRight)
    
    def getHitbox(self):
        return self.hitbox
    
    def gravity(self):
        self.yDelta += 0.5
        self.hitbox.y += self.yDelta
        if self.hitbox.y >= 600 - 40:
            self.hitbox.y = 600 - 40
            self.yDelta = 0

    def moveLeft(self):
        self.currentDirection = '<'

        self.frameCounter += 1
        if self.frameCounter % 6 == 0:
            self.updateWalkAnimationIndex()
            self.currentPlayerImg = self.getWalkImageLeft()

        self.hitbox.x -= 2
        if self.hitbox.x <= 0:
            self.hitbox.x = 0
    
    def moveRight(self):
        self.currentDirection = '>'

        self.frameCounter += 1
        if self.frameCounter % 6 == 0:
            self.updateWalkAnimationIndex()
            self.currentPlayerImg = self.getWalkImageRight()

        self.hitbox.x += 2
        if self.hitbox.x >= 800 - 22:
            self.hitbox.x = 800 - 22
    
    def movement(self):
        self.gravity()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveLeft()
            self.keyPressed = pygame.K_a
        elif keys[pygame.K_d]:
            self.moveRight()
            self.keyPressed = pygame.K_d
        elif keys[pygame.K_w]:
            # self.moveUp()
            self.keyPressed = pygame.K_w
        elif keys[pygame.K_s]:
            # self.moveDown()
            self.keyPressed = pygame.K_s
        else:
            self.aniIndex = 0
            self.frameCounter = 0

            if self.currentDirection == '>':
                self.currentPlayerImg = self.idleImageRight
            else:
                self.currentPlayerImg = self.idleImageLeft

            self.keyPressed = None
