import pyglet
from . import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):

    def __init__(self, game_window_size, *args, **kwargs):
        super().__init__(game_window_size, img=resources.bullet_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, 1.5)
        self.is_bullet = True

    def die(self, dt):
        self.dead = True