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

# Tiles
TILES = {"G": pygame.image.load("Assets\\Tiles\\Grass1.png"),
         "G2": pygame.image.load("Assets\\Tiles\\Grass2.png"),
         "W": pygame.image.load("Assets\\Tiles\\Water.png"),
         "T": pygame.image.load("Assets\\Tiles\\tall_grass.png"),
         "N": pygame.image.load("Assets\\Characters\\npc.png")}
TILE_ROW = ceil(X/SCALE)
TILE_COL = ceil(Y/SCALE)

# Paths
WORLD1_PATH = "Worlds\\World1.txt"
