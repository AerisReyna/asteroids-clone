import random
from . import asteroid

class Asteroids():
    
        
    def __init__(self, game_controller, num_asteroids, *args, **kwargs):
        self.gc = game_controller
        self.gen_asteroids(num_asteroids)

    def gen_asteroids(self, num_asteroids):
        for i in range(num_asteroids):
            asteroid_x, asteroid_y = self.gc.player_ship.position
            side = random.randint(0, 3)
            match side:
                case 0:
                    asteroid_y = self.gc.game_window.height
                    asteroid_x = random.randint(0, self.gc.game_window.width)
                case 1:
                    asteroid_x = self.gc.game_window.width
                    asteroid_y = random.randint(0, self.gc.game_window.height)
                case 2:
                    asteroid_y = 0
                    asteroid_x = random.randint(0, self.gc.game_window.width)
                case 3:
                    asteroid_x = 0
                    asteroid_y = random.randint(0, self.gc.game_window.height)
            new_asteroid = asteroid.Asteroid(self.gc, x=asteroid_x, y=asteroid_y)
            new_asteroid.rotation = random.randint(0, 360)
            new_asteroid.velocity_x = random.random() * 100
            new_asteroid.velocity_y = random.random() * 100
            self.gc.game_objects.append(new_asteroid)

    def reset(self):
        self.gen_asteroids(3)