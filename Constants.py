import pygame
from math import ceil

# Pygame screen variables
WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
X, Y = WIN.get_size()
SCALE = 50

# World variables
WORLD_WIDTH = 250
WORLD_HEIGHT = 250


# Enemy types
WATER = "water"
FIRE = "fire"
EARTH = "earth"

# Images
GRASS1_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Grass1.png"), (SCALE, SCALE))
GRASS2_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Grass2.png"), (SCALE, SCALE))
WATER_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Water.png"), (SCALE, SCALE))
TALL_GRASS_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\tall_grass.png"), (SCALE, SCALE))
NPC_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Characters\\npc.png"), (SCALE, SCALE))
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Characters\\player.png"), (SCALE, SCALE))

# Tiles
TILES = {"G": GRASS1_IMAGE,
         "G2": GRASS2_IMAGE,
         "W": WATER_IMAGE,
         "T": TALL_GRASS_IMAGE,
         "N": NPC_IMAGE}

WALKABLE_TILES = ["G", "G2", "T"]
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
