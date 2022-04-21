# I still need to move logic out of __init__ and make asteroids generate asteriods to add to the GC array. There's no reason for each thing to have it's own array if it has a reference to the GC

import pyglet
import random
from . import resources, physicalobject, util

class Asteroids():
    
        
    def __init__(self, game_controller, num_asteroids, *args, **kwargs):
        super().__init__(game_controller.game_window.get_size(), img=resources.asteroid_image, *args, **kwargs)
        self.gc = game_controller
        self.asteroids = []
        self.rotate_speed = random.random() * 100.0 - 50.0
        self.score_label = self.gc.score_label
        for i in range(num_asteroids):
            asteroid_x, asteroid_y = gc.player_ship.player_position
            while util.distance((asteroid_x, asteroid_y), player_position) < 100:
                asteroid_x = random.randint(0, 800)
                asteroid_y = random.randint(0, 600)
            new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, score_label=score_label, game_window_size=game_window_size, batch=batch)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = random.random() * 100
            new_asteroid.velocity_y = random.random() * 100
            asteroids.append(new_asteroid)

    def gen_asteroids(self, num):
