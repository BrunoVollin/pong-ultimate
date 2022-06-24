'''
Includes the Entity class.
'''
from abc import abstractmethod
import pygame as pg


class Entity(pg.sprite.Sprite):
    '''
    Basic class for both the paddle and the ball.
    '''

    def __init__(self, groups, pos, size, speed, color):
        super().__init__(groups)
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect
        self.direction = pg.math.Vector2(0, 0)
        self.speed = speed

    def update(self):
        '''
        Basic update method.
        '''
        self.input()
        self.move()

    @abstractmethod
    def input(self):
        '''
        Basic input method.
        '''
        raise NotImplementedError

    @abstractmethod
    def move(self):
        '''
        Basic movement method.
        '''
        raise NotImplementedError
