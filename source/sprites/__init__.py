'''
Includes the Ball and Paddle classes.
'''
import pygame as pg
import numpy as np

from source.constants import WIDTH, HEIGHT
from source.constants.palette import BALL_COLOR, P1_COLOR, P2_COLOR
from source.sprites.entity import Entity
from source.sprites.score import Score


class Ball(Entity):
    '''
    Class used to control the ball.
    '''

    def __init__(self, groups, paddles):
        super().__init__(groups, (WIDTH // 2, HEIGHT // 2), (15, 15), 5, BALL_COLOR)
        # Paddles
        self.paddles = paddles
        # Traits
        self.moving = False
        self.base_speed = 5
        # Paddle Collision SFX
        sound_1 = 'assets/sounds/4382__noisecollector__pongblipd-5.wav'
        self.paddle_collision_sfx = pg.mixer.Sound(sound_1)
        self.paddle_collision_sfx.set_volume(0.5)
        # Box Collision SFX
        sound_2 = 'assets/sounds/4383__noisecollector__pongblipd3.wav'
        self.box_collision_sfx = pg.mixer.Sound(sound_2)
        self.box_collision_sfx.set_volume(0.5)
        # Score SFX
        sound_3 = 'assets/sounds/Coin.mp3'
        self.score_up_sfx = pg.mixer.Sound(sound_3)
        self.score_up_sfx.set_volume(0.5)

    def input(self):
        '''
        Basic input method.
        Used to start moving the ball if it isn't already moving.
        '''
        if not self.moving:
            keys = pg.key.get_pressed()
            if keys[pg.K_SPACE]:
                random_x = np.random.choice([-1, 1])
                random_y = np.random.choice([-1, 1])
                self.direction.x = random_x
                self.direction.y = random_y
                self.speed = self.base_speed
                self.moving = True

    def move(self):
        '''
        Basic movement method.
        '''
        self.hitbox.x += self.direction.x * self.speed
        self.hitbox.y += self.direction.y * self.speed
        self.__box_collisions()
        self.__paddle_collisions()
        self.rect.center = self.hitbox.center

    def __box_collisions(self):
        '''
        Used to handle collisions with the walls.
        '''
        if self.hitbox.left <= 0 or self.hitbox.right >= WIDTH:
            side = 'right' if self.hitbox.left <= 0 else 'left'
            # Could be a lambda function but I'm dumb. lmao xD
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

    def __paddle_collisions(self):
        '''
        Used to handle collisions with the paddles.
        '''
        for paddle in self.paddles:
            if self.hitbox.colliderect(paddle.hitbox):
                self.direction.x *= -1
                self.hitbox.x += self.direction.x * self.speed
                self.hitbox.y += self.direction.y * self.speed
                self.paddle_collision_sfx.play()

    def increase_speed(self):
        '''
        Increases the speed of the ball by 1.
        '''
        self.speed += 1

    def is_moving(self):
        '''
        Checks if the ball is moving.
        '''
        return self.moving


class Paddle(Entity):
    '''
    Class used to control the paddles (players).
    '''

    def __init__(self, groups, side):
        if side == 'left':
            super().__init__(groups, (30, HEIGHT // 2), (10, 120), 4, P1_COLOR)
        elif side == 'right':
            super().__init__(groups, (WIDTH - 30, HEIGHT // 2), (10, 120), 4, P2_COLOR)
        self.score = Score(groups, side)
        self.side = side

    def input(self):
        '''
        Basic input method.
        '''
        keys = pg.key.get_pressed()
        if self.side == 'left':
            if keys[pg.K_w]:
                self.direction.y = -1
            elif keys[pg.K_s]:
                self.direction.y = 1
            else:
                self.direction.y = 0
        elif self.side == 'right':
            if keys[pg.K_UP]:
                self.direction.y = -1
            elif keys[pg.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0

    def move(self):
        '''
        Basic movement method.
        Used to move the paddle up and down.
        '''
        self.hitbox.y += self.direction.y * self.speed
        self.__box_collisions()
        self.rect.center = self.hitbox.center

    def __box_collisions(self):
        '''
        Used to handle collisions with the walls.
        '''
        if self.direction.y == -1 and self.rect.top <= 0:
            self.hitbox.top = 0
        elif self.direction.y == 1 and self.rect.bottom >= HEIGHT:
            self.hitbox.bottom = HEIGHT

    def increase_score(self):
        '''
        Increases the score of the player by 1.
        '''
        self.score.increase()

    def get_side(self):
        '''
        Returns the side of the paddle.
        '''
        return self.side
