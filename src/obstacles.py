import random
from . import constants  as con

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect_x = con.SCREEN_WIDTH
        self.rect_y = 0

    def update(self, speed: int):
        self.rect_x -= speed

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], (self.rect_x, self.rect_y))


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect_y = con.SMALL_CACTUS_Y


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect_y = con.LARGE_CACTUS_Y


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect_y = con.BIRD_Y
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], (self.rect_x, self.rect_y))
        self.index += 1