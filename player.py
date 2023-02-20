import pygame
from settings import *
from support import import_folder
from entity import Entity


class Player(Entity):
    def __init__(self, pos, group, obstacle_sprites, create_attack, destroy_weapon, create_magic):
        super().__init__(group)
        self.image = pygame.image.load('player1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.offset_visual = self.rect.inflate(0, -20)

        self.import_player_assets()
        self.state = 'down'

        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.create_attack = create_attack
        self.remedy_index = 0
        self.weapon = list(weapons.keys())[self.remedy_index]
        self.destroy_weapon = destroy_weapon
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 150
        self.magic_index = 0
        self.magic = list(magic_tools.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None
        self.create_magic = create_magic

        self.obstacle_sprites = obstacle_sprites

        self.stats = {'health': 100, 'energy': 50, 'healing_power': 10, 'magic': 5, 'speed': 5}
        self.health = self.stats['health'] * 0.5
        self.energy = self.stats['energy'] * 0.8
        self.speed = self.stats['speed']
        self.exp = 100

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
                style = list(magic_tools.keys())[self.magic_index]
                strength = list(magic_tools.vales())['strength'] + self.stats['magic']
                cost = list(magic_tools.vales())['cost']
                self.create_magic(style, strength, cost)
                #print('magic')

            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                if self.remedy_index < len(list(weapons.keys()))-1:
                    self.remedy_index += 1
                else:
                    self.remedy_index = 0
                self.weapon = list(weapons.keys())[self.remedy_index]

            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                if self.magic_index < len(list(magic_tools.keys()))-1:
                    self.magic_index += 1
                else:
                    self.magic_index = 0
                self.magic = list(magic_tools.keys())[self.magic_index]

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

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_weapon()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

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
