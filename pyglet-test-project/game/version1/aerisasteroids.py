import pyglet
from GameController import GameController

game_controller = GameController(window_size=(1920, 1080), fullscreen=True)

@game_controller.game_window.event
def on_draw():
    game_controller.game_window.clear()

    game_controller.draw()

pyglet.clock.schedule_interval(game_controller.update, 1/120.0)

if __name__ == '__main__':
    pyglet.app.run()
