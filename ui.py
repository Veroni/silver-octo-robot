import pygame
from settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.health_bar = pygame.Rect(10, 10, HEALTH_BAR_W, BAR_H)
        self.energy_bar = pygame.Rect(10, 35, ENERGY_BAR_W, BAR_H)
