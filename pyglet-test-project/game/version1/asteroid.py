import pyglet
from game import resources, load, player

main_batch = pyglet.graphics.Batch()

game_window = pyglet.window.Window(1800, 1000)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=game_window.height - 40, batch=main_batch)
level_label = pyglet.text.Label(text="An Amazing Game Tutorial", x=game_window.width//2, y=game_window.height - 40, anchor_x='center', batch=main_batch)

player_ship = player.Player(img=resources.player_image, game_window_size=game_window.get_size(), x=game_window.width//2, y=game_window.height//2, batch=main_batch)

asteroids = load.asteroids(3, game_window.get_size(), player_ship.position, main_batch)

player_lives = load.player_lives(3, game_window, main_batch)

game_objects = asteroids

game_objects.append(player_ship)

game_window.push_handlers(player_ship)

@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()

def update(dt):
    for obj in game_objects:
        obj.update(dt)

pyglet.clock.schedule_interval(update, 1/120.0)

if __name__ == '__main__':
    pyglet.app.run()
