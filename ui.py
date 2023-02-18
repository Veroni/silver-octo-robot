import pygame
from settings import *

class UI:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.health_bar = pygame.Rect(10, 10, HEALTH_BAR_W, BAR_H)
        self.energy_bar = pygame.Rect(10, 35, ENERGY_BAR_W, BAR_H)
        
        # converting remedy dict
        self.remedy_graphics = []
        for remedy in weapons.values():
            path = remedy['graphic']
            remedy = pygame.image.load(path).convert_alpha()
            self.remedy_graphics.append(remedy)
          
    def show_experience(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_EXP_COL)
        x = self.display_surface.get_size()[0] - 15 # offset 15 pix
        y = self.display_surface.get_size()[1] - 15 # offset 15 pix
        text_rect = text_surf.get_rect(bottomright=(x,y))
        
    def show_bar(self, current_amount, max_amount, bg, color):
        pygame.draw.rect(self.display_surface, BG_COL, bg)
        bar_ratio = current_amount / max_amount
        current_w = bg.width * bar_ratio
        current_rect = bg.copy()
        current_rect.width = current_w
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, BORDER_COL, current_rect, 2)
    
    def selection_box(self, left, top, has_switched):
        box_rect = pygame.Rect(left, top, ITEM_BAR, ITEM_BAR)
        pygame.draw.rect(self.display_surface, BG_COL, box_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, BORDER_COL_ACTIVE, box_rect, 2)
        else:
            pygame.draw.rect(self.display_surface, BORDER_COL, box_rect, 2)
        return box_rect
  
    def remedy_overlay(self, remedy_index, has_switched):
        box_rect = self.selection_box(10, 630, has_switched)
        remedy_surf = self.remedy_graphics[remedy_index]
        remedy_rect = remedy_surf.get_rect(center=box_rect.center)
        self.display_surface.blit(remedy_surf, remedy_rect)
        
    def display(self, player):
        # for debugging
        # pygame.draw.rect(self.display_surface, 'black', self.health_bar)
        self.show_bar(player.health, player.stats['health'],self.health_bar, HEALTH_COL)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar, ENERGY_COL)
        self.show_experience(player.exp)
        self.remedy_overlay(player.remedy_index, not player.can_switch_weapon)
