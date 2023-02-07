import pygame
from settings import *
from support import import_folder


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, obstacle_sprites, create_attack, destroy_weapon):
        super().__init__(group)
        self.image = pygame.image.load('player1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.offset_visual = self.rect.inflate(0, -20)

        self.import_player_assets()
        self.state = 'down'
        self.frame_index = 0
        self.anim_speed = 0.16

        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.weapon_index = 0
        self.weapon = list(weapons.keys())[self.weapon_index]
        self.destroy_weapon = destroy_weapon

        self.obstacle_sprites = obstacle_sprites

    def import_player_assets(self):
        char_path = './graphics/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
            'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []}

        for animation in self.animations.keys():
            full_path = char_path + animation
            self.animations[animation] = import_folder(full_path)
        #print(self.animations)

    def input(self):
        if not self.attacking:
            keys = pygame.key.get_pressed()

            # move
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.state = 'up'
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.state = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.state = 'left'
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.state = 'right'
            else:
                self.direction.x = 0

            # attack
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                #print('attack')

            # use magic
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                #print('magic')

    def get_state(self):
        # idle
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.state and not 'attack' in self.state:
                self.state = self.state + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.state:
                if 'idle' in self.state:
                    self.state = self.state.replace('_idle', '_attack')
                else:
                    self.state = self.state + '_attack'
        else:
            if 'attack' in self.state:
                self.state = self.state.replace('_attack', '')

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

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_weapon()

    def animate(self):
        animation = self.animations[self.state]

        # play animation
        self.frame_index += self.anim_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.offset_visual.center)

    def update(self):
        self.input()
        self.cooldowns()
        self.get_state()
        self.animate()
        self.move(self.speed)
