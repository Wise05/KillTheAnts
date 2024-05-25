import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # player is 33 x 60 px
        self.idleImageRight = r"C:\Users\zevan\Kill The Ants!\images\GregIdle.png"
        self.walkingPics = [
           r"C:\Users\zevan\Kill The Ants!\images\GregWalk1.png",
           r"C:\Users\zevan\Kill The Ants!\images\GregWalk2.png"
        ]
        self.crawlingImageRight = r"C:\Users\zevan\Kill The Ants!\images\GregCrawl.png"
        self.idleImageRight = pygame.image.load(self.idleImageRight).convert_alpha()
        self.walkImagesRight = [pygame.image.load(pic).convert_alpha() for pic in self.walkingPics]
        self.crawlingImageRight = pygame.image.load(self.crawlingImageRight).convert_alpha()
        self.idleImageRight = pygame.transform.scale(self.idleImageRight, (self.idleImageRight.get_width() * 1.5, self.idleImageRight.get_height() * 1.5))
        self.walkImagesRight = [pygame.transform.scale(pic, (self.idleImageRight.get_width(), self.idleImageRight.get_height())) for pic in self.walkImagesRight]
        self.crawlingImageRight = pygame.transform.scale(self.crawlingImageRight, (self.crawlingImageRight.get_width() * 1.5, self.crawlingImageRight.get_height() * 1.5))
        self.idleImageLeft = pygame.transform.flip(self.idleImageRight, True, False)
        self.walkImagesLeft = [pygame.transform.flip(pic, True, False) for pic in self.walkImagesRight]
        self.crawlingImageLeft = pygame.transform.flip(self.crawlingImageRight, True, False)
        self.normalHitbox = self.idleImageRight.get_rect()
        self.crawlHitbox = self.crawlingImageRight.get_rect()
        self.currentHitbox = self.normalHitbox
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
        return self.currentHitbox
    
    def gravity(self):
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
        if self.keyPressed == None: #and not ladder
            self.normalHitbox.y -= 6
        #todo! ladder mechanics

    def movement(self):
        self.gravity()
        dontMove = False

        
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
            self.aniIndex = 0
            self.frameCounter = 0
            self.currentHitbox = self.normalHitbox

            if self.currentDirection == '>':
                self.currentPlayerImg = self.idleImageRight
            else:
                self.currentPlayerImg = self.idleImageLeft

            self.keyPressed = None
