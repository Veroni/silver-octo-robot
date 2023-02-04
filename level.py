import pygame
from settings import *
from tile import Tile
from player import Player
from support import *
from random import choice


class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout("./graphics/map/map1.csv"),
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

        self.player = Player((2000, 1430), [self.visible_sprites], self.obstacle_sprites)
                    
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
