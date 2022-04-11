import pyglet

class PhysicalObject(pyglet.sprite.Sprite):
    
    def __init__(self, game_window_size, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.game_width = game_window_size[0]
        self.game_height = game_window_size[1]

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds_and_wrap()

    def check_bounds_and_wrap(self):
        min_x = -self.image.width / 2
        min_y = -self.image.height / 2
        max_x = self.game_width + self.image.width / 2
        max_y = self.game_height + self.image.width / 2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y > max_y:
            self.y = min_y
        elif self.y < min_y:
            self.y = max_y