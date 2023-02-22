import pygame
from settings import *
from entity import Entity

class Creature(Entity):
    def __init__(self, name, pos, groups):
        super.__init__(groups)
        self.sprite_type = 'creature'
        self.image = pygame.Surface((66,66))
        self.rect = self.image.get_rect(topleft=pos)
