import pygame as pg
import numpy as np
from source.model.entity import Entity
from source.utils.palette import BALL_COLOR
from source.utils.settings import WIDTH, HEIGHT


class Ball(Entity):
    def __init__(self, groups, paddles):
        super().__init__(groups, (WIDTH // 2, HEIGHT // 2), (15, 15), 5, BALL_COLOR)
        self.__paddles = paddles
        self.__moving = False
        sound_1 = "assets/sounds/4382__noisecollector__pongblipd-5.wav"
        sound_2 = "assets/sounds/4383__noisecollector__pongblipd3.wav"
        sound_3 = "assets/sounds/Coin.mp3"
        self.__paddle_collision_sfx = pg.mixer.Sound(sound_1)
        self.__paddle_collision_sfx.set_volume(0.5)
        self.__box_collision_sfx = pg.mixer.Sound(sound_2)
        self.__box_collision_sfx.set_volume(0.5)
        self.__score_up_sfx = pg.mixer.Sound(sound_3)
        self.__score_up_sfx.set_volume(0.5)

    def update(self):
        self.__input()
        self.__move()

    def __input(self):
        if not self.__moving:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                random_x = np.random.choice([-1, 1])
                random_y = np.random.choice([-1, 1])
                self._direction = pg.math.Vector2(random_x, random_y)
                self._speed = self._base_speed
                self.__moving = True

    def __move(self):
        self._hitbox.x += self._direction.x * self._speed
        self._hitbox.y += self._direction.y * self._speed
        self.__box_collisions()
        self.__paddle_collisions()
        self.rect.center = self._hitbox.center

    def __box_collisions(self):
        if self._hitbox.left <= 0 or self._hitbox.right >= WIDTH:
            side = "right" if self._hitbox.left <= 0 else "left"
            # Could be a lambda function but I'm dumb lmao
            for paddle in self.__paddles:
                if paddle.get_side() == side:
                    paddle.increase_score()
                    self.__score_up_sfx.play()
            self._hitbox.center = (WIDTH // 2, HEIGHT // 2)
            self._direction.x = 0
            self._direction.y = 0
            self.__moving = False
        if self._hitbox.top <= 0 or self._hitbox.bottom >= HEIGHT:
            self._direction.y *= -1
            self.__box_collision_sfx.play()

    def __paddle_collisions(self):
        for paddle in self.__paddles:
            if self._hitbox.colliderect(paddle._hitbox):
                self._direction.x *= -1
                self._hitbox.x += self._direction.x * self._speed
                self._hitbox.y += self._direction.y * self._speed
                self.__paddle_collision_sfx.play()

    def increase_speed(self):
        self._speed += 1

    def is_moving(self):
        return self.__moving
