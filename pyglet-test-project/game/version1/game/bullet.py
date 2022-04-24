import pyglet
from . import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):

    def __init__(self, game_controller, *args, **kwargs):
        super().__init__(game_controller, img=resources.bullet_image, *args, **kwargs)
        pyglet.clock.schedule_once(self.die, .75)
        self.is_bullet = True

    def die(self, dt):
        self.dead = True