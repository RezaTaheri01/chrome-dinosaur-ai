import os
import pygame

# Global Constants
PLAYER_MODE = True

# BG_COLOR = (25, 30, 55) # Navy Blue
# FORE_COLOR = (255, 255, 255) # White

FORE_COLOR = (25, 30, 55) # Navy Blue
BG_COLOR = (255, 255, 255) # White

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600


# Load Assets
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

# Start Speed
GAME_SPEED = 20

FPS = 30

CLOUD_X_RNG = (50, 100)
CLOUD_Y_RNG = (50, 100)

# Dino
X_POS = 210
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 8.5


BIRD_Y = 250
SMALL_CACTUS_Y = 325
LARGE_CACTUS_Y = 300

OBSTACLES_MAX_GAP = 750
OBSTACLES_MIN_GAP = 525
OBSTACLES_GAP_REDUCER = 20


MAX_OBSTACLES = (SCREEN_WIDTH // OBSTACLES_MIN_GAP) + 2
