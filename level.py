import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice


class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = SortCamGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.current_attack = None

        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout("./graphics/map/map2.csv"),
            'grass': import_csv_layout("./graphics/map/map_Grass.csv"),
            'object': import_csv_layout("./graphics/map/map_LargeObjects.csv")
        }
        graphics = {
            'grass': import_folder('./graphics/grass'),
            'objects': import_folder('./graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            # for debugging
                            # Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'invisible')
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'grass':
                            rand_grass_img = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'grass', rand_grass_img)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                        if style == 'entity':
                            if col == '394':
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_weapon,
                                    self.create_magic)
                            else:
                                Creature('friend', (x, y), [self.visible_sprites])
        
    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites])

    def destroy_weapon(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None
    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
        
class SortCamGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_screen_x = self.display_surface.get_size()[0] // 2
        self.half_screen_y = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating a map
        self.map_floor = pygame.image.load("./graphics/tilemap/map2.png").convert()
        self.map_rect = self.map_floor.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_screen_x
        self.offset.y = player.rect.centery - self.half_screen_y

        # drawing the map
        map_offset = self.map_rect.topleft - self.offset
        self.display_surface.blit(self.map_floor, map_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)
            
