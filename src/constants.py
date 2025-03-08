import os
import pygame

# Initialize Pygame
pygame.init()

# Dark
BG_COLOR = (25, 30, 55) # Navy Blue
FORE_COLOR = (255, 255, 255) # White
# Light
# FORE_COLOR = (25, 30, 55)  # Navy Blue
# BG_COLOR = (255, 255, 255)  # White

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("Dino Runner")

# Load Assets
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
                pygame.image.load(os.path.join(
                    "Assets/Cactus", "SmallCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
                pygame.image.load(os.path.join(
                    "Assets/Cactus", "LargeCactus2.png")),
                pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
        pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))

GAME_SPEED = 20
FPS = 30

# Dinosaur
X_POS = 210
Y_POS = 310
Y_POS_DUCK = 340
JUMP_VEL = 7.5

# Background
X_POS_BG = 0
Y_POS_BG = 380

# Obstacles
SPAWN_CHANCE = 0.05

BIRD_Y = 255
SMALL_CACTUS_Y = 325
LARGE_CACTUS_Y = 300
OBSTACLES_MIN_GAP = 600
CLOUD_X_RNG = (50, 100)
CLOUD_Y_RNG = (50, 100)

FONT = pygame.font.Font('freesansbold.ttf', 20)
MENU_FONT = pygame.font.Font('freesansbold.ttf', 30)

INCREASE_SPEED_DIV = 150
MIN_GAP_INCREASE = 5

# NEAT
FPS_AI = 0  # set it to Zero for max speed

NEGATIVE_FITNESS = -1
POSITIVE_FITNESS = 2.75
BONUS_FITNESS = 0.075

SCORE_LIMIT = 10_000
MAX_GEN = 50
SPAWN_CHANCE_AI = 0.05
GAME_SPEED_AI = 20
