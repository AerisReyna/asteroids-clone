import pyglet
import math
from pyglet.window import key
from . import physicalobject, resources, bullet, asteroid



class Player(physicalobject.PhysicalObject):

    def __init__(self, game_controller, *args, **kwargs):
        super().__init__(game_controller, img=resources.player_image, *args, **kwargs)
        self.gc = game_controller
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, batch=game_controller.main_batch, *args, **kwargs)
        self.engine_sprite.visible = False

        self.reacts_to_bullets = False
        
        self.key_handler = key.KeyStateHandler()
        
        self.max_thrust = 300.0
        self.max_rotation = 200.0
        self.current_thrust = 0
        self.current_rotation = 0
        self.thrust_interval = 15
        self.rotation_interval = 20
        self.bullet_speed = 300

    def reset(self):
        self.current_thrust = 0
        self.current_rotation = 0
        self.x = self.game_width / 2
        self.y = self.game_height / 2
        self.rotation = 0
        self.velocity_x = 0
        self.velocity_y = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()

    def update(self, dt):
        super(Player, self).update(dt)

        if self.key_handler[key.LEFT]:
            if self.current_rotation < self.max_rotation:
                self.current_rotation += self.rotation_interval
            self.rotation -= self.current_rotation * dt
        if self.key_handler[key.RIGHT]:
            if self.current_rotation < self.max_rotation:
                self.current_rotation += self.rotation_interval
            self.rotation += self.current_rotation * dt
        if self.key_handler[key.UP]:
            if self.current_thrust < self.max_thrust:
                self.current_thrust += self.thrust_interval
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.current_thrust * dt
            force_y = math.sin(angle_radians) * self.current_thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False
        # if self.key_handler[key.DOWN]:
        #     if self.current_thrust > 0:
        #         self.current_thrust -= self.thrust_interval
        #     angle_radians = -math.radians(self.rotation)
        #     force_x = math.cos(angle_radians) * self.max_thrust * dt
        #     force_y = math.sin(angle_radians) * self.max_thrust * dt
        #     self.velocity_x -= force_x
        #     self.velocity_y -= force_y

    def fire(self):
        angle_radians = -math.radians(self.rotation)
        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(self.gc, x=bullet_x, y=bullet_y)
        bullet_vx = (
            self.velocity_x +
            math.cos(angle_radians) * self.bullet_speed
        )
        bullet_vy = (
            self.velocity_y +
            math.sin(angle_radians) * self.bullet_speed
        )
        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy
        self.gc.game_objects.append(new_bullet)
        
    def handle_collision_with(self, other_object):
        if type(other_object) is asteroid.Asteroid:
            if self.gc.player_lives.lose_life():
                self.dead = True
                self.gc.game_over = True
            else:
                self.reset()
        else:
            print('here')
            self.dead = False

    def delete(self):
        self.engine_sprite.delete()
        super(Player, self).delete()