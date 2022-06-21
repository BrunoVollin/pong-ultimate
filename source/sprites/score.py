'''
Contains the Score class.
'''
import pygame as pg
from source.constants import WIDTH, HEIGHT
from source.constants.palette import P1_COLOR, P2_COLOR


class Score(pg.sprite.Sprite):
    '''
    This class is used to display scores.
    '''

    def __init__(self, groups, paddle_side):
        super().__init__(groups)
        self.font = pg.font.Font('assets/fonts/dotty/dotty.ttf', 256)
        self.total = 0
        if paddle_side == 'left':
            self.pos = WIDTH // 4, HEIGHT // 2
            self.color = P1_COLOR
        elif paddle_side == 'right':
            self.pos = WIDTH * 3 // 4, HEIGHT // 2
            self.color = P2_COLOR
        else:
            raise ValueError('paddle_side must be either "left" or "right".')
        self.update()

    def update(self):
        '''
        Basic update method.
        '''
        self.image = self.font.render(str(self.total), False, self.color)
        self.rect = self.image.get_rect(center=self.pos)

    def increase(self):
        '''
        Increases the score by 1.
        '''
        self.total += 1
