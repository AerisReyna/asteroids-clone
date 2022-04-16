from hashlib import new
import pyglet
import random
from . import resources, physicalobject, util, asteroid


def asteroids(num_asteroids, game_window_size, player_position, score_label, batch=None):
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, score_label=score_label, game_window_size=game_window_size, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 100
        new_asteroid.velocity_y = random.random() * 100
        asteroids.append(new_asteroid)
    return asteroids