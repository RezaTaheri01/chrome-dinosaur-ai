import random
from . import constants  as con

image = con.CLOUD
width = image.get_width()


class Cloud:
    def __init__(self, power):
        self.x = con.SCREEN_WIDTH + \
            random.randint(con.CLOUD_X_RNG[0] * power, con.CLOUD_X_RNG[1] * power)
        self.y = random.randint(con.CLOUD_Y_RNG[0], con.CLOUD_Y_RNG[1])
        # self.image = con.CLOUD
        # self.width = self.image.get_width()

    def update(self, speed: int):
        self.x -= speed
        if self.x < -width:
            self.x = con.SCREEN_WIDTH + \
                random.randint(con.CLOUD_X_RNG[0], con.CLOUD_X_RNG[1])
            self.y = random.randint(con.CLOUD_Y_RNG[0], con.CLOUD_Y_RNG[1])

    def draw(self, SCREEN):
        SCREEN.blit(image, (self.x, self.y))
