import pygame

class Remedy(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.state.split('_')[0]
        full_path = f'./graphics/remedy/{player.remedy}/{direction}.png'
        self.image = pygame.image.load(full_path).convert_alpha()
        
        # origin
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 15))
        elif direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 15))
        elif direction == 'down':
            self.rect = self.image.get_rect(midtop=player.rect.midbottom + pygame.math.Vector2(-1, 0))
        elif direction == 'up':
            self.rect = self.image.get_rect(midbottom=player.rect.midtop + pygame.math.Vector2(1, 0))
        else:
            self.rect = self.image.get_rect(center = player.rect.center)
