# Todo: Balance between min_gap and game_speed
import os
import pickle
import neat
import pygame
import random
from collections import deque

from src.player import Dinosaur
from src.obstacles import SmallCactus, LargeCactus, Bird
from src.cloud import Cloud
from src import constants as con


spawn_chance = con.SPAWN_CHANCE_AI
generation = 0
min_gap = con.OBSTACLES_MIN_GAP

dinosaurs: list[Dinosaur] = []
nets = []
ge = []
highest = 0


class ScoreReachedException(Exception):
    pass


def main(config_path):
    pygame.init()
    run(config_path)
    pygame.quit()


def run(config_file):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes, con.MAX_GEN)
    print(f'\nBest genome:\n{winner}')
    print(f'\nHighest Score:\n{highest}')


def eval_genomes(genomes, config):
    global generation, highest
    
    # with open("results.txt", "a") as file:
    #     file.write(f"Gen: {generation}, Highest: {highest}\n")
        
    generation += 1

    clock = pygame.time.Clock()
    dinosaurs.clear()
    nets.clear()
    ge.clear()
    obstacles = deque([])
    clouds = [Cloud(power * 6) for power in range(1, 4)]

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        dinosaurs.append(Dinosaur())
        g.fitness = 0
        ge.append(g)

    game_speed = con.GAME_SPEED_AI
    points = 0
    x_pos_bg, y_pos_bg = con.X_POS_BG, con.Y_POS_BG

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        run = handle_events()
        con.SCREEN.fill(con.BG_COLOR)

        x_pos_bg = draw_background(x_pos_bg, y_pos_bg, game_speed)

        obstacle_index = get_next_obstacle_index(dinosaurs, obstacles)

        if not dinosaurs:
            for g in ge:
                g.fitness -= con.NEGATIVE_FITNESS
            run = False
            break

        for x, dino in enumerate(dinosaurs):
            ge[x].fitness += con.BONUS_FITNESS
            dino.draw(con.SCREEN)
            mode = "d"  # Duck
            if obstacle_index != -1:
                # Calculate time until collision
                time_until_collision = (
                    obstacles[obstacle_index].rect_x - dino.dino_rect_x) / game_speed
                output = nets[x].activate((
                    time_until_collision,
                    dino.dino_rect_y,
                    obstacles[obstacle_index].rect_y,
                    obstacles[obstacle_index].image[0].get_width(),
                    obstacles[obstacle_index].image[0].get_height()
                ))
                if output[0] > 0.5:
                    mode = "j"  # Jump
            dino.update(mode)

        manage_obstacles(obstacles, game_speed)
        manage_clouds(clouds, game_speed)
        points, game_speed = update_score(points, game_speed, len(dinosaurs))

        clock.tick(con.FPS_AI)
        
            
        pygame.display.update()

        if points > con.SCORE_LIMIT:
            # highest = points
            save_best_genome(config)


def get_next_obstacle_index(dinosaurs, obstacles):
    if dinosaurs:
        for i, obstacle in enumerate(obstacles):
            if dinosaurs[0].dino_rect_x < obstacle.rect_x + obstacle.image[0].get_width():
                return i
    return -1


def save_best_genome(config):
    best_genome = max(ge, key=lambda g: g.fitness)
    best_net = neat.nn.FeedForwardNetwork.create(best_genome, config)
    pickle.dump(best_net, open("best.pickle", "wb"))
    raise ScoreReachedException(
        f"Score reached {con.SCORE_LIMIT} — stopping training!")


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


def update_score(points, game_speed, alive):
    global min_gap
    points += 1
    
    if not con.STABLE_SPEED_AI:
        if points % con.INCREASE_SPEED_DIV == 0:
            game_speed += con.GAME_SPEED_PLUS_AI
            
            # min_gap += con.MIN_GAP_INCREASE
            min_gap += (min_gap // con.GAP_DIV) + 1

    render_text(f"Points: {points}", (1000, 40))
    render_text(f"Gen: {generation}", (80, 40))
    render_text(f"Alive: {alive}", (80, 80))

    return points, game_speed


def render_text(text, position):
    rendered_text = con.FONT.render(text, True, con.FORE_COLOR)
    con.SCREEN.blit(rendered_text, rendered_text.get_rect(center=position))


def manage_obstacles(obstacles, game_speed):
    if obstacles and obstacles[0].rect_x < 0:
        obstacles.popleft()
        for g in ge:
            g.fitness += con.POSITIVE_FITNESS

    if random.random() < spawn_chance:
        if not obstacles or con.SCREEN_WIDTH - obstacles[-1].rect_x >= min_gap:
            obstacles.append(random.choice([
                SmallCactus(con.SMALL_CACTUS),
                LargeCactus(con.LARGE_CACTUS),
                Bird(con.BIRD)
            ]))

    for i, obstacle in enumerate(obstacles):
        obstacle.draw(con.SCREEN)
        obstacle.update(game_speed)
        check_dino_collision(i, obstacle)


def check_dino_collision(index, obstacle: LargeCactus):
    for i, dino in enumerate(dinosaurs):
        if check_collision(dino, obstacle):
            ge[i].fitness -= con.NEGATIVE_FITNESS
            dinosaurs.pop(i)
            nets.pop(i)
            ge.pop(i)


def check_collision(player, obstacle):
    offset_x = obstacle.rect_x - player.dino_rect_x
    offset_y = obstacle.rect_y - player.dino_rect_y
    return player.get_mask().overlap(pygame.mask.from_surface(obstacle.image[0]), (offset_x, offset_y))


def manage_clouds(clouds, game_speed):
    for cloud in clouds:
        cloud.draw(con.SCREEN)
        cloud.update(game_speed // 2)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config-feedforward.txt")
    main(config_path)
