import pyglet
from . import resources

class Lives():
    def __init__(self, num, game_window_size, batch=None):
        self.player_lives = []
        for i in range(num):
            new_sprite = pyglet.sprite.Sprite(img=resources.player_image, x=game_window_size[0]-(i+1)*30, y=game_window_size[1]-30, batch=batch)
            new_sprite.scale = 0.5
            new_sprite.rotation = -90
            self.player_lives.append(new_sprite)

    def lose_life(self):
        if len(self.player_lives) > 0:
            self.player_lives.pop()
            return False
        else:
            return True