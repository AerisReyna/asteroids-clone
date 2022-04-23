# I still need to move logic out of __init__ and make asteroids generate asteriods to add to the GC array. There's no reason for each thing to have it's own array if it has a reference to the GC

import pyglet
import random
from . import resources, util, asteroid

class Asteroids():
    
        
    def __init__(self, game_controller, num_asteroids, *args, **kwargs):
        self.gc = game_controller
        self.gen_asteroids(num_asteroids)

    def gen_asteroids(self, num_asteroids):
        for i in range(num_asteroids):
            asteroid_x, asteroid_y = self.gc.player_ship.position
            while util.distance((asteroid_x, asteroid_y), self.gc.player_ship.position) < 100:
                asteroid_x = random.randint(0, 800)
                asteroid_y = random.randint(0, 600)
            new_asteroid = asteroid.Asteroid(self.gc, x=asteroid_x, y=asteroid_y)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = random.random() * 100
            new_asteroid.velocity_y = random.random() * 100
            self.gc.game_objects.append(new_asteroid)