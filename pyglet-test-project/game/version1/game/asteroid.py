import pyglet
import random
from . import resources, physicalobject

class Asteroid(physicalobject.PhysicalObject):
    def __init__(self, game_window_size, *args, **kwargs):
        super().__init__(game_window_size, img=resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100.0 - 50.0

    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        if self.dead and self.scale > 0.25:
            num_asteroids = random.randint(2, 3)
            for i in range(num_asteroids):
                new_asteroid = Asteroid(game_window_size=(self.game_width, self.game_height), x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = (random.random() * 70 + self.velocity_x)
                new_asteroid.velocity_y = (random.random() * 70 + self.velocity_y)
                new_asteroid.scale = self.scale * .5
                self.new_objects.append(new_asteroid)

    def update(self, dt):
        super().update(dt)
        self.rotation += self.rotate_speed * dt