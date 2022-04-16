import pyglet
from game import resources, load, player, score, lives

main_batch = pyglet.graphics.Batch()
game_window = pyglet.window.Window(1800, 1000)

score_label = score.ScoreLabel(text="Score: 0", x=10, y=game_window.height - 40, batch=main_batch)
level_label = pyglet.text.Label(text="Aeris Asteroids", x=game_window.width//2, y=game_window.height - 40, anchor_x='center', batch=main_batch)

player_lives = lives.Lives(3, game_window.get_size(), main_batch)
player_ship = player.Player(player_lives=player_lives, game_window_size=game_window.get_size(), x=game_window.width//2, y=game_window.height//2, batch=main_batch)

asteroids = load.asteroids(3, game_window.get_size(), player_ship.position, score_label, main_batch)


game_objects = asteroids

game_objects.append(player_ship)


game_window.push_handlers(player_ship.key_handler)
game_window.push_handlers(player_ship.on_key_press)

@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()

def update(dt):
    for i in range(len(game_objects)):
        for j in range(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)
    
    to_add = []

    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []
    
    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_remove.delete()
        game_objects.remove(to_remove)

    game_objects.extend(to_add)

pyglet.clock.schedule_interval(update, 1/120.0)

if __name__ == '__main__':
    pyglet.app.run()
