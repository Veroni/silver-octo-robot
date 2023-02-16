import pygame
from settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.health_bar = pygame.Rect(10, 10, HEALTH_BAR_W, BAR_H)
        self.energy_bar = pygame.Rect(10, 35, ENERGY_BAR_W, BAR_H)
    
    def display(self, player):
        # for debugging
        # pygame.draw.rect(self.display_surface, 'black', self.health_bar)
        self.show_bar(player.health, player.stats['health'],self.health_bar, HEALTH_COL)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar, ENERGY_COL)
        
    def show_bar(self, current_amount, max_amount, bg, color):
        pygame.draw.rect(self.display_surface, BG_COL, bg)
        bar_ratio = current_amount / max_amount
        current_w = bg.width * bar_ratio
        current_rect = bg.copy()
        current_rect.width = current_w
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, BORDER_COL, current_rect, 2)
