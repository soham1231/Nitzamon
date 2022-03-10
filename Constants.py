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
TILE_ROW = ceil(X/SCALE)
TILE_COL = ceil(Y/SCALE)

# Paths
WORLD1_PATH = "Worlds\\World1.txt"

FPS = 20
fps = FPS  # Not a constant but idk where to put it
