# game settings

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64

BAR_H = 18
HEALTH_BAR_W = 180
ENERGY_BAR_W = 160
ITEM_BAR = 80
UI_FONT = './graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

WATER_COL = '#71ddee'
BG_COL = '#222222'
BORDER_COL = '#111111'
TEXT_COL = '#EEEEEE'
TEXT_EXP_COL = '#71ddee'
HEALTH_COL = 'pink'
ENERGY_COL = 'cyan'
BORDER_COL_ACTIVE = 'gold'

weapons = {
    'sword': {'cooldown': 100, 'healing': 15, 'graphic':'./graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'healing': 25, 'graphic':'./graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'healing': 25, 'graphic':'./graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 400, 'healing': 25, 'graphic':'./graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 400, 'healing': 25, 'graphic':'./graphics/weapons/sai/full.png'},
}

magic_tools = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': './graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 15, 'graphic': './graphics/particles/heal/heal.png'}
}

WORLD_MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
]
