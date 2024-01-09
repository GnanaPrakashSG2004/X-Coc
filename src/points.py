BLANK = "0"
WALL = "1"
SPAWN = "2"
TOWNHALL = "3"
HUT = "4"
CANNON = "5"
WIZARD_TOWER = "6"
WALL_TOP = "1"
WALL_BOTTOM = "1"
WALL_LEFT = "1"
WALL_RIGHT = "1"
WALL_TOPRIGHT = "1"
WALL_TOPLEFT = "1"
WALL_BOTTOMRIGHT = "1"
WALL_BOTTOMLEFT = "1"

HERO_POS = [0,0]
hero = 1
movement = 1 # 1 = dont break wall, 2 = break wall

troop_limit = {
    'barbarian': 10,
    'dragon': 3,
    'balloon': 5,
    'archer': 7,
    'stealth_archer': 3,
    'healer': 1
}


config = {
    'dimensions': (18,36),
    'spawn_points': [(0,0),(17,0),(0,35)],
    'town_hall': (6,16),
    'huts': [(6,11),(10,4),(16,15),(6,30),(6,22)],
    'cannons': [(10,22),(12,13), (3,5)],
    'wizard_towers': [(7,27),(17,27)],
    'walls_top': [(3,10),(3,11),(3,12),(3,13),(3,14),(3,15),(3,16),(3,17),(3,18),(3,19),(3,20),(3,21),(3,22),(3,23),(3,24),(3,25)],
    'walls_bottom': [(15,10),(15,11),(15,12),(15,13),(15,14),(15,15),(15,16),(15,17),(15,18),(15,19),(15,20),(15,21),(15,22),(15,23),(15,24),(15,25),(3,26)],
    'walls_left': [(4,9),(5,9),(6,9),(7,9),(8,9),(9,9),(10,9),(11,9),(12,9),(13,9),(14,9),(15,9)],
    'walls_right': [(3,26),(4,26),(5,26),(6,26),(7,26),(8,26),(9,26),(10,26),(11,26),(12,26),(13,26),(14,26)],
    'walls_topright': [(3,26)],
    'walls_topleft': [(3,9)],
    'walls_bottomright': [(15,26)],
    'walls_bottomleft': [(4,9)],
    'hero_pos': (17,35),
}

config_level_1 = {
    'dimensions': (18,36),
    'spawn_points': [(0,0),(17,0),(0,35)],
    'town_hall': (6,16),
    'huts': [(6,11),(10,4),(16,15),(6,30),(6,22)],
    'cannons': [{ "position": (10,22), "level": 1 },{ "position": (12,13), "level": 1 }],
    'wizard_towers': [{ "position": (7,27), "level": 1 },{ "position": (17,27), "level": 1 }],
    'walls_top': [{ "position": (3, 10), "level": 1 }, { "position": (3, 11), "level": 1 }, { "position": (3, 12), "level": 1 }, { "position": (3, 13), "level": 1 }, { "position": (3, 14), "level": 1 }, { "position": (3, 15), "level": 1 }, { "position": (3, 16), "level": 1 }, { "position": (3, 17), "level": 1 }, { "position": (3, 18), "level": 1 }, { "position": (3, 19), "level": 1 }, { "position": (3, 20), "level": 1 }, { "position": (3, 21), "level": 1 }, { "position": (3, 22), "level": 1 }, { "position": (3, 23), "level": 1 }, { "position": (3, 24), "level": 1 }, { "position": (3, 25), "level": 1 }],
    'walls_bottom': [{ "position": (15, 10), "level": 1 }, { "position": (15, 11), "level": 1 }, { "position": (15, 12), "level": 1 }, { "position": (15, 13), "level": 1 }, { "position": (15, 14), "level": 1 }, { "position": (15, 15), "level": 1 }, { "position": (15, 16), "level": 1 }, { "position": (15, 17), "level": 1 }, { "position": (15, 18), "level": 1 }, { "position": (15, 19), "level": 1 }, { "position": (15, 20), "level": 1 }, { "position": (15, 21), "level": 1 }, { "position": (15, 22), "level": 1 }, { "position": (15, 23), "level": 1 }, { "position": (15, 24), "level": 1 }, { "position": (15, 25), "level": 1 }, { "position": (3, 26), "level": 1 }],
    'walls_left': [{ "position": (4, 9), "level": 2 }, { "position": (5, 9), "level": 2 }, { "position": (6, 9), "level": 2 }, { "position": (7, 9), "level": 2 }, { "position": (8, 9), "level": 2 }, { "position": (9, 9), "level": 2 }, { "position": (10, 9), "level": 2 }, { "position": (11, 9), "level": 2 }, { "position": (12, 9), "level": 2 }, { "position": (13, 9), "level": 2 }, { "position": (14, 9), "level": 2 }, { "position": (15, 9), "level": 2 }],
    'walls_right': [{ "position": (3, 26), "level": 1 }, { "position": (4, 26), "level": 1 }, { "position": (5, 26), "level": 1 }, { "position": (6, 26), "level": 1 }, { "position": (7, 26), "level": 1 }, { "position": (8, 26), "level": 1 }, { "position": (9, 26), "level": 1 }, { "position": (10, 26), "level": 1 }, { "position": (11, 26), "level": 1 }, { "position": (12, 26), "level": 1 }, { "position": (13, 26), "level": 1 }, { "position": (14, 26), "level": 1 }],
    'walls_topright': [{ "position": (3, 26), "level": 1 }],
    'walls_topleft': [{ "position": (3, 9), "level": 2 }],
    'walls_bottomright': [{ "position": (15, 26), "level": 1 }],
    'walls_bottomleft': [{ "position": (4, 9), "level": 2 }],
    'hero_pos': (17,35),
}
config_level_2 = {
    'dimensions': (18,36),
    'spawn_points': [(0,0),(17,0),(0,35)],
    'town_hall': (6,16),
    'huts': [(6,11),(10,4),(16,15),(6,30),(6,22)],
    'cannons': [{ "position": (10,22), "level": 2 }, { "position": (12,13), "level": 3 }, { "position": (3,5), "level": 4 }],
    'wizard_towers': [{ "position": (7,27), "level": 2 }, { "position": (17,27), "level": 3 }, { "position": (7,0), "level": 3 }],
    'walls_top': [{ "position": (3, 10), "level": 2 }, { "position": (3, 11), "level": 2 }, { "position": (3, 12), "level": 2 }, { "position": (3, 13), "level": 2 }, { "position": (3, 14), "level": 2 }, { "position": (3, 15), "level": 2 }, { "position": (3, 16), "level": 2 }, { "position": (3, 17), "level": 2 }, { "position": (3, 18), "level": 2 }, { "position": (3, 19), "level": 2 }, { "position": (3, 20), "level": 2 }, { "position": (3, 21), "level": 2 }, { "position": (3, 22), "level": 2 }, { "position": (3, 23), "level": 2 }, { "position": (3, 24), "level": 2 }, { "position": (3, 25), "level": 2 }],
    'walls_bottom': [{ "position": (15, 10), "level": 2 }, { "position": (15, 11), "level": 2 }, { "position": (15, 12), "level": 2 }, { "position": (15, 13), "level": 2 }, { "position": (15, 14), "level": 2 }, { "position": (15, 15), "level": 2 }, { "position": (15, 16), "level": 2 }, { "position": (15, 17), "level": 2 }, { "position": (15, 18), "level": 2 }, { "position": (15, 19), "level": 2 }, { "position": (15, 20), "level": 2 }, { "position": (15, 21), "level": 2 }, { "position": (15, 22), "level": 2 }, { "position": (15, 23), "level": 2 }, { "position": (15, 24), "level": 2 }, { "position": (15, 25), "level": 2 }, { "position": (3, 26), "level": 2 }],
    'walls_left': [{ "position": (4, 9), "level": 2 }, { "position": (5, 9), "level": 2 }, { "position": (6, 9), "level": 2 }, { "position": (7, 9), "level": 2 }, { "position": (8, 9), "level": 2 }, { "position": (9, 9), "level": 2 }, { "position": (10, 9), "level": 2 }, { "position": (11, 9), "level": 2 }, { "position": (12, 9), "level": 2 }, { "position": (13, 9), "level": 2 }, { "position": (14, 9), "level": 2 }, { "position": (15, 9), "level": 2 }],
    'walls_right': [{ "position": (3, 26), "level": 3 }, { "position": (4, 26), "level": 3 }, { "position": (5, 26), "level": 3 }, { "position": (6, 26), "level": 3 }, { "position": (7, 26), "level": 3 }, { "position": (8, 26), "level": 3 }, { "position": (9, 26), "level": 3 }, { "position": (10, 26), "level": 3 }, { "position": (11, 26), "level": 3 }, { "position": (12, 26), "level": 3 }, { "position": (13, 26), "level": 3 }, { "position": (14, 26), "level": 3 }],
    'walls_topright': [{ "position": (3, 26), "level": 3 }],
    'walls_topleft': [{ "position": (3, 9), "level": 2 }],
    'walls_bottomright': [{ "position": (15, 26), "level": 3 }],
    'walls_bottomleft': [{ "position": (4, 9), "level": 2 }],
    'hero_pos': (17,35),
}
config_level_3 = {
    'dimensions': (18,36),
    'spawn_points': [(0,0),(17,0),(0,35)],
    'town_hall': (6,16),
    'huts': [(6,11),(10,4),(16,15),(6,30),(6,22)],
    'cannons': [{ "position": (10,22), "level": 4 }, { "position": (12,13), "level": 5 }, { "position": (3,5), "level": 4 }, { "position": (0,19), "level": 5 }],
    'wizard_towers': [{ "position": (7,27), "level": 4 }, { "position": (17,27), "level": 5 }, { "position": (6,1), "level": 4 }, { "position": (15,2), "level": 5 }],
    'walls_top': [{ "position": (3, 10), "level": 5 }, { "position": (3, 11), "level": 5 }, { "position": (3, 12), "level": 5 }, { "position": (3, 13), "level": 5 }, { "position": (3, 14), "level": 5 }, { "position": (3, 15), "level": 5 }, { "position": (3, 16), "level": 5 }, { "position": (3, 17), "level": 5 }, { "position": (3, 18), "level": 5 }, { "position": (3, 19), "level": 5 }, { "position": (3, 20), "level": 5 }, { "position": (3, 21), "level": 5 }, { "position": (3, 22), "level": 5 }, { "position": (3, 23), "level": 5 }, { "position": (3, 24), "level": 5 }, { "position": (3, 25), "level": 5 }],
    'walls_bottom': [{ "position": (15, 10), "level": 5 }, { "position": (15, 11), "level": 5 }, { "position": (15, 12), "level": 5 }, { "position": (15, 13), "level": 5 }, { "position": (15, 14), "level": 5 }, { "position": (15, 15), "level": 5 }, { "position": (15, 16), "level": 5 }, { "position": (15, 17), "level": 5 }, { "position": (15, 18), "level": 5 }, { "position": (15, 19), "level": 5 }, { "position": (15, 20), "level": 5 }, { "position": (15, 21), "level": 5 }, { "position": (15, 22), "level": 5 }, { "position": (15, 23), "level": 5 }, { "position": (15, 24), "level": 5 }, { "position": (15, 25), "level": 5 }, { "position": (3, 26), "level": 5 }],
    'walls_left': [{ "position": (4, 9), "level": 5 }, { "position": (5, 9), "level": 5 }, { "position": (6, 9), "level": 5 }, { "position": (7, 9), "level": 5 }, { "position": (8, 9), "level": 5 }, { "position": (9, 9), "level": 5 }, { "position": (10, 9), "level": 5 }, { "position": (11, 9), "level": 5 }, { "position": (12, 9), "level": 5 }, { "position": (13, 9), "level": 5 }, { "position": (14, 9), "level": 5 }, { "position": (15, 9), "level": 5 }],
    'walls_right': [{ "position": (3, 26), "level": 4 }, { "position": (4, 26), "level": 4 }, { "position": (5, 26), "level": 4 }, { "position": (6, 26), "level": 4 }, { "position": (7, 26), "level": 4 }, { "position": (8, 26), "level": 4 }, { "position": (9, 26), "level": 4 }, { "position": (10, 26), "level": 4 }, { "position": (11, 26), "level": 4 }, { "position": (12, 26), "level": 4 }, { "position": (13, 26), "level": 4 }, { "position": (14, 26), "level": 4 }],
    'walls_topright': [{ "position": (3, 26), "level": 4 }],
    'walls_topleft': [{ "position": (3, 9), "level": 5 }],
    'walls_bottomright': [{ "position": (15, 26), "level": 4 }],
    'walls_bottomleft': [{ "position": (4, 9), "level": 5 }],
    'hero_pos': (17,35),
}
