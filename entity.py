import pygame

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.anim_speed = 0.16
        self.direction = pygame.math.Vector2()

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


