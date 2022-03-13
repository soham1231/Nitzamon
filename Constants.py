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
LOG_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\log.png"), (SCALE, SCALE))
LEAVES_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\leaves.png"), (SCALE, SCALE))
BORDER_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Tiles\\Borded.png"), (SCALE, SCALE))

NPC_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Characters\\npc.png"), (SCALE, SCALE))
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("Assets\\Characters\\player.png"), (SCALE, SCALE))

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
