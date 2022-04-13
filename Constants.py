import pygame
from math import ceil
from Classes.NitzamonClasses.Move import Move
from Classes.NitzamonClasses.Nitzamon import Nitzamon

pygame.init()
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

X, Y = WIN.get_size()
SCALE = 50
MINI_SCALE = 7

# World variables
WORLD_WIDTH = 250
WORLD_HEIGHT = 250

# Nitzamon
WATER = "water"
FIRE = "fire"
EARTH = "earth"
COMMENTAR = "Commentar"
GEM_TRIO = "Gem trio"
MASMERION = "Masmerion"
NITZAPHONE = "Nitzaphone"
HEARTIAN = "Heartian"
SHAREE = "Sharee"
DARK_SQUARION = "Dark squarion"
MANAGEREON = "Managereon"
PENTAGEON = "Pentageon"
HEADEA = "Headea"
TRION = "Trion"
WORKERY = "Workery"
NAMES = [COMMENTAR, GEM_TRIO, MASMERION, NITZAPHONE, HEARTIAN, SHAREE, DARK_SQUARION, MANAGEREON, PENTAGEON,
         HEADEA, TRION]
NITZAMON_ELEMENTS_DICT = {COMMENTAR: WATER,
                          GEM_TRIO: FIRE,
                          MASMERION: EARTH,
                          NITZAPHONE: WATER,
                          HEARTIAN: FIRE,
                          SHAREE: WATER,
                          DARK_SQUARION: FIRE,
                          MANAGEREON: EARTH,
                          PENTAGEON: WATER,
                          HEADEA: FIRE,
                          TRION: EARTH,
                          WORKERY: EARTH}
# Moves
SCRATCH = Move("normal", 9, "Scratch", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Scratch.mp3"))
PUNCH = Move("normal", 10, "Punch", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Punch.mp3"))
SLASH = Move("normal", 11, "Slash", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Slash.mp3"))
BURN = Move(FIRE, 10, "Burn", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Burn.mp3"))
FIREBALL = Move(FIRE, 11, "Fire-ball", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Fireball.mp3"))
LASER = Move(FIRE, 12, "Laser", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Laser.mp3"))
EARTHQUAKE = Move(EARTH, 12, "Earthquake", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Earthquake.mp3"))
ROCKSLIDE = Move(EARTH, 11, "RockSlide", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Rockslide.mp3"))
LEAFBLADE = Move(EARTH, 10, "LeafBlade", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Leafblade.mp3"))
WATERFALL = Move(WATER, 12, "Waterfall", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Waterfall.mp3"))
SPIT = Move(WATER, 10, "Spit", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Spit.mp3"))
GEYSER = Move(WATER, 11, "Geyser", pygame.mixer.Sound("Assets\\Sounds\\Moves\\Geyser.mp3"))

FIRE_MOVES = [FIREBALL, LASER, BURN]
EARTH_MOVES = [EARTHQUAKE, LEAFBLADE, ROCKSLIDE]
WATER_MOVES = [SPIT, WATERFALL, GEYSER]
NORMAL_MOVES = [SCRATCH, PUNCH, SLASH]

# Starters
NITZAPHONE_STARTER = Nitzamon(NITZAPHONE, 5, [SCRATCH, SLASH, WATERFALL, SPIT])
GEM_TRIO_STARTER = Nitzamon(GEM_TRIO, 5, [PUNCH, SLASH, BURN, LASER])
MASMERION_STARTER = Nitzamon(MASMERION, 5, [SCRATCH, PUNCH, EARTHQUAKE, ROCKSLIDE])

# Nitzaballs
NITZABALL_CHANCES = {"Normal": 0.1,
                     "Gem": 0.2,
                     "Phone": 0.4,
                     "Masmer": 0.6,
                     "Ultimate": 1}

# Images
GRASS1_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Grass1.png"), (SCALE, SCALE))
GRASS2_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Grass2.png"), (SCALE, SCALE))
WATER_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Water1.png"), (SCALE, SCALE))
TALL_GRASS_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\tall_grass.png"), (SCALE, SCALE))
LOG_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\log.png"), (SCALE, SCALE))
LEAVES_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\leaves.png"), (SCALE, SCALE))
BORDER_IMAGE = pygame.transform.scale(pygame.image.load("Assets/Tiles/Border.png"), (SCALE, SCALE))

NPC_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Characters\\npc.png"), (SCALE, SCALE))
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Characters\\player.png"), (SCALE, SCALE))
NPC_SPRITE_RONI = pygame.transform.scale(pygame.image.load("Assets\\Characters\\NPCS\\Roni.jpg"), (SCALE, SCALE))
NPC_PFP_RONI = pygame.transform.scale(pygame.image.load("Assets/Characters/NPCS/Roni_pfp.jpg"), (int(X / 4), int(Y / 4)))
GILAD_NPC = pygame.transform.scale(pygame.image.load("Assets\\Characters\\gilad.png"), (SCALE + 5, SCALE + 5))
GILAD_PFP = pygame.transform.scale(pygame.image.load("Assets\\Characters\\Gilad_pfp.png"), (int(X / 4), int(Y / 4)))
SHOHAM_NPC = pygame.transform.scale(pygame.image.load("Assets\\Characters\\shoham.png"), (SCALE + 5, SCALE + 5))
SHOHAM_PFP = pygame.transform.scale(pygame.image.load("Assets\\Characters\\Shoham_pfp.png"), (int(X / 4), int(Y / 4)))
ADI_NPC = pygame.transform.scale(pygame.image.load("Assets\\Characters\\adi.png"), (SCALE + 5, SCALE + 5))
ADI_PFP = pygame.transform.scale(pygame.image.load("Assets\\Characters\\Adi_pfp.png"), (int(X / 4), int(Y / 4)))


# Tiles
TILES = {"G": GRASS1_IMAGE,
         "g": GRASS2_IMAGE,
         "W": WATER_IMAGE,
         "T": TALL_GRASS_IMAGE,
         "N": NPC_IMAGE,
         "L": LOG_IMAGE,
         "l": LEAVES_IMAGE,
         "B": BORDER_IMAGE}

WALKABLE_TILES = ["G", "g", "T", "l"]
TILE_ROW = ceil(X/SCALE)
TILE_COL = ceil(Y/SCALE)

# Paths
WORLD1_PATH = "Worlds\\World1.txt"

FPS = 20
fps = FPS  # Not a constant but i don't know where to put it

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (60, 60, 60)
HOVER_COLOR = (30, 30, 30)

# Fight
FIGHT_COOL_DOWN = 5
FIGHT_FONT_SIZE = 32

# Main Menu
MENU_FONT_SIZE = 32
NITZAMON_FONT_SIZE = 64
