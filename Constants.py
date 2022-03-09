import pygame

# Pygame screen variables
X = 1000
Y = 700
SCALE = 20
WIN = pygame.display.set_mode((X, Y))

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
TILE_ROW = int(X/SCALE)
TILE_COL = int(Y/SCALE)
