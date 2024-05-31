import pygame

class SpriteObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    
    def loadSprite(self, path):
        sprite = pygame.image.load(path).convert_alpha()
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * 1.65, sprite.get_height() * 1.65))
        return sprite
    
    