import pygame
from . import constants  as con

duck_img = con.DUCKING
run_img = con.RUNNING
jump_img = con.JUMPING

class Dinosaur:
    def __init__(self):
        # Default is Duck
        self.dino_run = False
        self.dino_duck = True
        self.dino_jump = False

        self.step_index = 0
        self.image = run_img[0]
        self.jump_vel = con.JUMP_VEL
        self.dino_rect_x = con.X_POS
        self.dino_rect_y = con.Y_POS

    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        elif self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        elif userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

    def duck(self):
        self.image = duck_img[self.step_index // 5]
        self.dino_rect_x = con.X_POS
        self.dino_rect_y = con.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.image = run_img[self.step_index // 5]
        self.dino_rect_x = con.X_POS
        self.dino_rect_y = con.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = jump_img
        if self.dino_jump:
            self.dino_rect_y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -con.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = con.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect_x, self.dino_rect_y))
        
    def get_mask(self):
        return pygame.mask.from_surface(self.image)

