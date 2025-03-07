import pygame
import random
from src.player import Dinosaur
from src.obstacles import SmallCactus, LargeCactus, Bird
from src.cloud import Cloud
from src import constants as con
from collections import deque


# Initialize Pygame
pygame.init()

SCREEN = pygame.display.set_mode(
    (con.SCREEN_WIDTH, con.SCREEN_HEIGHT), pygame.DOUBLEBUF)
pygame.display.set_caption("Dino Runner")


def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    clock = pygame.time.Clock()
    player = Dinosaur()
    clouds = [Cloud(power * 6) for power in range(1, 4)]
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = deque([])
    death_count = 0
    obstacle_distance = con.OBSTACLES_MAX_GAP
    current_gap = con.OBSTACLES_MAX_GAP
    reduce_point = game_speed + 10

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, con.FORE_COLOR)
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = con.BG.get_width()

        SCREEN.fill(con.BG_COLOR)

        SCREEN.blit(con.BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(con.BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        SCREEN.fill(con.BG_COLOR)

        background()
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) > con.MAX_OBSTACLES:
            obstacles.popleft()

        if obstacle_distance >= current_gap:
            obstacle_distance = 0
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                obstacles.append(SmallCactus(con.SMALL_CACTUS))
            elif obstacle_type == 1:
                obstacles.append(LargeCactus(con.LARGE_CACTUS))
            elif obstacle_type == 2:
                obstacles.append(Bird(con.BIRD))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update(game_speed, obstacles)

            # Mask collision detection
            offset_x = obstacle.rect_x - player.dino_rect_x
            offset_y = obstacle.rect_y - player.dino_rect_y

            player_mask = player.get_mask()
            obstacle_mask = pygame.mask.from_surface(
                obstacle.image[0])  # Create mask for the obstacle

            if player_mask.overlap(obstacle_mask, (offset_x, offset_y,)):
                pygame.time.delay(1000)
                death_count += 1
                run = False
                menu(death_count)

        for cloud in clouds:
            cloud.draw(SCREEN)
            cloud.update(game_speed // 2)

        score()

        obstacle_distance += game_speed

        # each time that the condition be True we decrease obstacles gap
        if game_speed == reduce_point:
            reduce_point += 10
            current_gap -= con.OBSTACLES_GAP_REDUCER
            if current_gap < con.OBSTACLES_MIN_GAP:
                current_gap = con.OBSTACLES_MIN_GAP

        clock.tick(30)
        pygame.display.update()


def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill(con.BG_COLOR)
        font = pygame.font.Font('freesansbold.ttf', 30)
        # Display restart instructions

        if death_count == 0:
            text = font.render("Press any Key to Start", True, con.FORE_COLOR)
        elif death_count > 0:
            text = font.render("Press any Key to Restart",
                               True, con.FORE_COLOR)
            score = font.render(
                "Your Score: " + str(points), True, con.FORE_COLOR)
            scoreRect = score.get_rect()
            scoreRect.center = (con.SCREEN_WIDTH // 2,
                                con.SCREEN_HEIGHT // 2 + 50)
            SCREEN.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (con.SCREEN_WIDTH // 2, con.SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        SCREEN.blit(
            con.RUNNING[0], (con.SCREEN_WIDTH // 2 - 20, con.SCREEN_HEIGHT // 2 - 140))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.quit()
                main()


if __name__ == "__main__":
    if con.PLAYER_MODE:
        menu(death_count=0)
