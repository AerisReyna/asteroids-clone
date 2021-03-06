import pyglet
from game import player, score, lives, asteroids, gameover
from pyglet.window import key

class GameController():

    def __init__(self, window_size=(800, 600), num_lives=3, *args, **kwargs):
        self.main_batch = pyglet.graphics.Batch()
        self.game_over = False
        self.game_over_batch = pyglet.graphics.Batch()
        self.game_objects = []
        self.game_window = pyglet.window.Window(fullscreen=True)
        self.score_label = score.ScoreLabel(text="Score: 0", x=10, 
                                            y=self.game_window.height - 40, 
                                            batch=self.main_batch)
        self.game_over_screen = gameover.GameOver(self, self.game_over_batch)
        self.level_label = pyglet.text.Label(text="Aeris Asteroids", 
                                                x=self.game_window.width//2, 
                                                y=self.game_window.height - 40, 
                                                anchor_x='center', 
                                                batch=self.main_batch)
        self.player_lives = lives.Lives(num_lives, self.game_window.get_size(), self.main_batch)
        self.player_ship = player.Player(self, x=self.game_window.width//2, y=self.game_window.height//2)
        self.asteroids = asteroids.Asteroids(self, 3)

        self.game_objects.append(self.player_ship)

        self.game_window.push_handlers(self.player_ship.key_handler)
        self.game_window.push_handlers(self.on_key_press)

    def draw(self):
        if self.game_over:
            self.game_over_screen.score()
            self.game_over_batch.draw()
        else:
            self.main_batch.draw()

    def update(self, dt):
        if self.game_over == True:
            pass
        else:
            for i in range(len(self.game_objects)):
                for j in range(i+1, len(self.game_objects)):
                    obj_1 = self.game_objects[i]
                    obj_2 = self.game_objects[j]
                    if not obj_1.dead and not obj_2.dead:
                        if obj_1.collides_with(obj_2):
                            obj_1.handle_collision_with(obj_2)
                            obj_2.handle_collision_with(obj_1)
        

            for obj in self.game_objects:
                obj.update(dt)

        
            for to_remove in [obj for obj in self.game_objects if obj.dead]:
                to_remove.delete()
                self.game_objects.remove(to_remove)

    def restart(self):
        self.game_over = False
        for obj in self.game_objects:
            obj.delete()
        self.game_objects = []
        self.player_ship = player.Player(self, x=self.game_window.width//2, y=self.game_window.height//2)
        self.game_objects.append(self.player_ship)
        self.game_window.push_handlers(self.player_ship.key_handler)
        self.score_label.text = "Score: 0"
        self.player_lives.reset()
        self.player_ship.reset()
        self.asteroids.reset()

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.player_ship.fire()
        if symbol == key.ENTER:
            self.restart()
