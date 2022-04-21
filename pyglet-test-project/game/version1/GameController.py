import pyglet
from game import load, player, score, lives

class GameController():

    def __init__(self, window_size=(800, 600), num_lives=3):
        self.main_batch = pyglet.graphics.Batch()
        self.game_window = pyglet.window.Window(width=window_size[0], height=window_size[1])
        self.score_label = score.ScoreLabel(text="Score: 0", x=10, 
                                            y=self.game_window.height - 40, 
                                            batch=self.main_batch)
        self.level_label = pyglet.text.Label(text="Aeris Asteroids", 
                                                x=self.game_window.width//2, 
                                                y=self.game_window.height - 40, 
                                                anchor_x='center', 
                                                batch=self.main_batch)
        self.player_lives = lives.Lives(num_lives, self.game_window.get_size(), self.main_batch)
        self.player_ship = player.Player(player_lives=self.player_lives, game_window_size=self.game_window.get_size(), x=self.game_window.width//2, y=self.game_window.height//2, batch=self.main_batch)
        self.asteroids = load.asteroids(3, self.game_window.get_size(), self.player_ship.position, self.score_label, self.main_batch)

        self.game_objects = self.asteroids
        self.game_objects.append(self.player_ship)

        self.game_window.push_handlers(self.player_ship.key_handler)
        self.game_window.push_handlers(self.player_ship.on_key_press)

    def update(self, dt):
        for i in range(len(self.game_objects)):
            for j in range(i+1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                if not obj_1.dead and not obj_2.dead:
                    if obj_1.collides_with(obj_2):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)
    
        to_add = []

        for obj in self.game_objects:
            obj.update(dt)
            to_add.extend(obj.new_objects)
            obj.new_objects = []
    
        for to_remove in [obj for obj in self.game_objects if obj.dead]:
            to_remove.delete()
            self.game_objects.remove(to_remove)

        self.game_objects.extend(to_add)