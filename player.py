import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites):
        super().__init__(group)
        self.image = pygame.image.load('player1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.offset_visual = self.rect.inflate(0, -20)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.offset_visual.x += self.direction.x * speed
        self.collision('horizontal')
        self.offset_visual.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.offset_visual.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.offset_visual.colliderect(self.offset_visual):
                    if self.direction.x > 0:
                        self.offset_visual.right = sprite.offset_visual.left
                    if self.direction.x < 0:
                        self.offset_visual.left = sprite.offset_visual.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.offset_visual.colliderect(self.offset_visual):
                    if self.direction.y > 0:
                        self.offset_visual.bottom = sprite.offset_visual.top
                    if self.direction.y < 0:
                        self.offset_visual.top = sprite.offset_visual.bottom

    def update(self):
        self.input()
        self.move(self.speed)

