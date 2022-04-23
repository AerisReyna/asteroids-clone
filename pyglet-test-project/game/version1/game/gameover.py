import pyglet
from pyglet.window import key

class GameOver():
    def __init__(self, game_controller, batch):
        self.gc = game_controller
        self.game_over_text = pyglet.text.Label(text="Game Over", font_size=200, batch=batch, anchor_x='center', anchor_y='center', x=game_controller.game_window.width/2, y=game_controller.game_window.height - 250)
        self.score_text = pyglet.text.Label(text="Final " + game_controller.score_label.text, font_size=50, batch=batch, anchor_x='center', anchor_y='center', x=game_controller.game_window.width/2, y=game_controller.game_window.height - 500)
        self.restart_text = pyglet.text.Label(text="Press [enter] to restart. Press [esc] to quit.", font_size=50, batch=batch, anchor_x='center', anchor_y='center', x=game_controller.game_window.width/2, y=game_controller.game_window.height - 650)
        # self.background = pyglet.shapes.Rectangle(0, 0, self.gc.game_window.width, self.gc.game_window.height, color=(60, 0, 120), batch=batch)

    def score(self):
        self.score_text.text= "Final " + self.gc.score_label.text

    def on_key_press(self, symbol, modifiers):
        if symbol == key.ENTER:
            self.gc.restart()