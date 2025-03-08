import pygame
import random

from src.player import Dinosaur
from src.obstacles import SmallCactus, LargeCactus, Bird
from src.cloud import Cloud
from src import constants as con
from collections import deque

spawn_chance = 0.1 # 10%

def main():
    pygame.init()
    run_game()
    pygame.quit()


def run_game():
    clock = pygame.time.Clock()
    player = Dinosaur()
    clouds = [Cloud(power * 6) for power in range(1, 4)]
    obstacles = deque([])

    game_speed = 20
    points = 0
    death_count = 0

    x_pos_bg = con.X_POS_BG
    y_pos_bg = con.Y_POS_BG

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                
        run = handle_events()
        con.SCREEN.fill(con.BG_COLOR)

        x_pos_bg = draw_background(x_pos_bg, y_pos_bg, game_speed)
        player.draw(con.SCREEN)
        player.update(pygame.key.get_pressed())

        manage_obstacles(obstacles, player, game_speed,
                         death_count, points)
        manage_clouds(clouds, game_speed)
        points, game_speed = update_score(points, game_speed)

        clock.tick(con.FPS)
        pygame.display.update()


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def draw_background(x_pos_bg, y_pos_bg, game_speed):
    image_width = con.BG.get_width()
    con.SCREEN.blit(con.BG, (x_pos_bg, y_pos_bg))
    con.SCREEN.blit(con.BG, (image_width + x_pos_bg, y_pos_bg))
    return 0 if x_pos_bg <= -image_width else x_pos_bg - game_speed


def update_score(points, game_speed):
    points += 1
    if points % 100 == 0:
        game_speed += 1

    text = con.FONT.render(f"Points: {points}", True, con.FORE_COLOR)
    con.SCREEN.blit(text, text.get_rect(center=(1000, 40)))
    return points, game_speed


def manage_obstacles(obstacles, player, game_speed, death_count, points):
    if obstacles and obstacles[0].rect_x < 0:
        obstacles.popleft()

    if random.random() < spawn_chance:  # Random chance to spawn obstacle
        if not obstacles or con.SCREEN_WIDTH - obstacles[-1].rect_x + obstacles[-1].image[0].get_width() >= con.OBSTACLES_MIN_GAP:
            obstacles.append(random.choice([
                SmallCactus(con.SMALL_CACTUS),
                LargeCactus(con.LARGE_CACTUS),
                Bird(con.BIRD)
            ]))

    for obstacle in obstacles:
        obstacle.draw(con.SCREEN)
        obstacle.update(game_speed)
        if check_collision(player, obstacle):
            pygame.time.delay(1000)
            menu(death_count + 1, points)


def check_collision(player, obstacle):
    offset_x = obstacle.rect_x - player.dino_rect_x
    offset_y = obstacle.rect_y - player.dino_rect_y
    return player.get_mask().overlap(pygame.mask.from_surface(obstacle.image[0]), (offset_x, offset_y))


def manage_clouds(clouds, game_speed):
    for cloud in clouds:
        cloud.draw(con.SCREEN)
        cloud.update(game_speed // 2)


def menu(death_count, points):
    run = True
    while run:
        con.SCREEN.fill(con.BG_COLOR)
        font = con.MENU_FONT

        text = font.render("Press any Key to Start" if death_count ==
                           0 else "Press any Key to Restart", True, con.FORE_COLOR)
        con.SCREEN.blit(text, text.get_rect(
            center=(con.con.SCREEN_WIDTH // 2, con.con.SCREEN_HEIGHT // 2)))

        if death_count > 0:
            score_text = font.render(
                f"Your Score: {points}", True, con.FORE_COLOR)
            con.SCREEN.blit(score_text, score_text.get_rect(
                center=(con.con.SCREEN_WIDTH // 2, con.con.SCREEN_HEIGHT // 2 + 50)))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                main()


if __name__ == "__main__":
    main()
