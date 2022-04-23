import pyglet
from . import resources

class Lives():
    def __init__(self, num, game_window_size, batch=None):
        self.player_lives = []
        self.total_lives = num
        self.game_window_size = game_window_size
        self.batch = batch
        self.reset()

    def lose_life(self):
        if len(self.player_lives) > 0:
            self.player_lives.pop()
            return False
        else:
            return True

    def reset(self):
        for i in range(self.total_lives):
            new_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=self.game_window_size[0]-(i+1)*30, y=self.game_window_size[1]-30, batch=self.batch)
            new_sprite.scale = 0.5
            new_sprite.rotation = -90
            self.player_lives.append(new_sprite)