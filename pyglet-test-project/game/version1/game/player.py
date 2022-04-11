import pyglet
from pyglet.window import key
from . import physicalobject, resources



class Player(physicalobject.PhysicalObject):

    def __init__(self, game_window_size, *args, **kwargs):
        super().__init__(game_window_size, *args, **kwargs)

        self.max_thrust = 300.0
        self.max_rotation = 200.0
        self.current_thrust = 0
        self.current_rotation = 0
        self.thrust_interval = 30
        self.rotation_interval = 20
        self.keys = dict(left=False, right=False, up=False, down=False)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False

    def update(self, dt):
        super(Player, self).update(dt)

        if self.keys['left']:
            if self.current_rotation < self.max_rotation:
                self.current_rotation += self.rotation_interval
            self.rotation -= self.current_rotation * dt
        if self.keys['right']:
            if self.current_rotation < self.max_rotation:
                self.current_rotation += self.rotation_interval
            self.rotation += self.current_rotation * dt