import pygame
from objects import SpriteObject

class Player(SpriteObject.SpriteObject):
    def __init__(self, x, y):
        super().__init__()
        # player is 23 x 40 px
        self.idleImageRight = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\GregIdle.png")
        self.walkingImages = [
           r"C:\Users\zevan\Kill The Ants!\images\GregWalk1.png",
           r"C:\Users\zevan\Kill The Ants!\images\GregWalk2.png"
        ]
        self.walkImagesRight = [self.loadSprite(img) for img in self.walkingImages]
        self.crawlingImageRight = self.loadSprite(r"C:\Users\zevan\Kill The Ants!\images\GregCrawl.png")
        self.idleImageLeft = pygame.transform.flip(self.idleImageRight, True, False)
        self.walkImagesLeft = [pygame.transform.flip(pic, True, False) for pic in self.walkImagesRight]
        self.crawlingImageLeft = pygame.transform.flip(self.crawlingImageRight, True, False)


        self.normalHitbox = self.idleImageRight.get_rect()
        self.crawlHitbox = self.crawlingImageRight.get_rect()
        # Can be changed based on whether or not the character is crouching
        self.currentHitbox = self.normalHitbox
        self.normalHitbox.x = x
        self.normalHitbox.y = y

        # Holds the current walking frame 
        self.animationFrameIndex = 0
        # Holds the number of frames from the game
        self.frameCounter = 0
        
        self.currentDirection = '>'
        self.currentPlayerImg = self.idleImageRight

        self.xDelta = 0
        self.yDelta = 0
        self.keyPressed = None


        self.touchesLadder = False
    
    def getWalkImageRight(self):
        return self.walkImagesRight[self.animationFrameIndex]

    def getWalkImageLeft(self):
        return self.walkImagesLeft[self.animationFrameIndex]
    
    def getPlayerSprite(self):
        return self.currentPlayerImg
    
    def updateWalkAnimationIndex(self):
        self.animationFrameIndex = (self.animationFrameIndex + 1) % len(self.walkImagesRight)
    
    def getHitbox(self):
        return self.currentHitbox
    
    def gravity(self):
        if not self.touchesLadder:
            self.yDelta += 0.5
            self.currentHitbox.y += self.yDelta
            if self.currentHitbox.y >= 600 - self.currentHitbox.height:
                self.currentHitbox.y = 600 - self.currentHitbox.height
                self.yDelta = 0

    def moveLeft(self):
        self.currentDirection = '<'

        self.frameCounter += 1
        if self.frameCounter % 12 == 0:
            self.updateWalkAnimationIndex()
            self.currentPlayerImg = self.getWalkImageLeft()

        self.currentHitbox.x -= 2
        if self.currentHitbox.x <= 0:
            self.currentHitbox.x = 0
    
    def moveRight(self):
        self.currentDirection = '>'

        self.frameCounter += 1
        if self.frameCounter % 12 == 0:
            self.updateWalkAnimationIndex()
            self.currentPlayerImg = self.getWalkImageRight()

        self.currentHitbox.x += 2
        if self.currentHitbox.x >= 800 - 22:
            self.currentHitbox.x = 800 - 22
    
    def crawl(self):
        self.crawlHitbox.x = self.currentHitbox.x
        self.crawlHitbox.y = self.currentHitbox.y
        if self.currentDirection == '>':
            self.currentPlayerImg = self.crawlingImageRight
        else:
            self.currentPlayerImg = self.crawlingImageLeft
        self.currentHitbox = self.crawlHitbox

    def moveUp(self):
        if self.touchesLadder:
            self.currentHitbox.y -= 1.5
        elif self.keyPressed == None and not self.touchesLadder: 
            self.currentHitbox.y -= 6
        

    def movement(self):
        self.gravity()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and not keys[pygame.K_s]:
            self.currentHitbox = self.normalHitbox
            self.moveLeft()
            self.keyPressed = pygame.K_a
        elif keys[pygame.K_d] and not keys[pygame.K_s]:
            self.currentHitbox = self.normalHitbox
            self.moveRight()
            self.keyPressed = pygame.K_d
        elif keys[pygame.K_w]:
            self.moveUp()
            self.keyPressed = pygame.K_w
        elif keys[pygame.K_s]:
            self.crawl()
            self.keyPressed = pygame.K_s
        else:
            self.animationFrameIndex = 0
            self.frameCounter = 0
            self.currentHitbox = self.normalHitbox

            if self.currentDirection == '>':
                self.currentPlayerImg = self.idleImageRight
            else:
                self.currentPlayerImg = self.idleImageLeft

            self.keyPressed = None

    def setTouchesLadder(self, boo):
        self.touchesLadder = boo
