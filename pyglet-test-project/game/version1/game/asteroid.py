import pyglet
import random
from . import resources, physicalobject

class Asteroid(physicalobject.PhysicalObject):
    def __init__(self, num, game_window_size, score_label, *args, **kwargs):
        super().__init__(game_window_size, img=resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100.0 - 50.0
        self.score_label = score_label
        

    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        if self.dead:
            self.score_label.increment()
        if self.dead and self.scale > 0.25:
            num_asteroids = random.randint(2, 3)
            for i in range(num_asteroids):
                new_asteroid = Asteroid(game_window_size=(self.game_width, self.game_height), x=self.x, y=self.y, batch=self.batch, score_label=self.score_label)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = (random.random() * 70 + self.velocity_x)
                new_asteroid.velocity_y = (random.random() * 70 + self.velocity_y)
                new_asteroid.scale = self.scale * .5
                self.new_objects.append(new_asteroid)

    def update(self, dt):
        super().update(dt)
        self.rotation += self.rotate_speed * dt