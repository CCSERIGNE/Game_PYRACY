import pygame

from game import GREEN, GREY, YELLOW


class Speedway(pygame.sprite.Sprite):
    position = True

    def __init__(self, width, height):
        super().__init__()

#        self.image = pygame.Surface([width, height])
        
#        self.image.fill(GREY)
#        self.image.set_colorkey(GREY)
        
        self.image = pygame.image.load('black-car.png').convert_alpha()
        pygame.draw.rect(self.image, GREEN, [0, 0, width*0.1, height])
        pygame.draw.rect(self.image, GREEN, [width*0.9, 0, width, height])
        pygame.draw.rect(self.image, YELLOW, [width*0.48, 0, width*0.04, height])
        self.rect = self.image.get_rect()
        
