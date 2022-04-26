import pygame as pg
import numpy as np
from source.model.entity import Entity
from source.utils.palette import BALL_COLOR
from source.utils.settings import WIDTH, HEIGHT


class Ball(Entity):
    def __init__(self, categories, paddles):
        super().__init__(categories, (WIDTH // 2, HEIGHT // 2), (15, 15), 5, BALL_COLOR)
        self.paddles = paddles
        self.moving = False
        sound_1 = "assets/sounds/4382__noisecollector__pongblipd-5.wav"
        sound_2 = "assets/sounds/4383__noisecollector__pongblipd3.wav"
        sound_3 = "assets/sounds/Coin.mp3"
        self.paddle_collision_sfx = pg.mixer.Sound(sound_1)
        self.paddle_collision_sfx.set_volume(0.5)
        self.box_collision_sfx = pg.mixer.Sound(sound_2)
        self.box_collision_sfx.set_volume(0.5)
        self.score_up_sfx = pg.mixer.Sound(sound_3)
        self.score_up_sfx.set_volume(0.5)

    def update(self):
        self._input()
        self._move()

    def _input(self):
        if not self.moving:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                random_x = np.random.choice([-1, 1])
                random_y = np.random.choice([-1, 1])
                self.direction = pg.math.Vector2(random_x, random_y)
                self.speed = self.base_speed
                self.moving = True

    def _move(self):
        self.hitbox.x += self.direction.x * self.speed
        self.hitbox.y += self.direction.y * self.speed
        self._box_collisions()
        self._paddle_collisions()
        self.rect.center = self.hitbox.center

    def _box_collisions(self):
        if self.hitbox.left <= 0 or self.hitbox.right >= WIDTH:
            side = "right" if self.hitbox.left <= 0 else "left"
            # Could be a lambda function but I'm dumb lmao
            for paddle in self.paddles:
                if paddle.get_side() == side:
                    paddle.increase_score()
                    self.score_up_sfx.play()
            self.hitbox.center = (WIDTH // 2, HEIGHT // 2)
            self.direction.x = 0
            self.direction.y = 0
            self.moving = False
        if self.hitbox.top <= 0 or self.hitbox.bottom >= HEIGHT:
            self.direction.y *= -1
            self.box_collision_sfx.play()

    def _paddle_collisions(self):
        for paddle in self.paddles:
            if self.hitbox.colliderect(paddle.hitbox):
                self.direction.x *= -1
                self.hitbox.x += self.direction.x * self.speed
                self.hitbox.y += self.direction.y * self.speed
                self.paddle_collision_sfx.play()

    def increase_speed(self):
        self.speed += 1

    def is_moving(self, condition=True):
        return self.moving == condition
