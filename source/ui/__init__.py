'''
Includes the User Interface class.
'''
import pygame as pg
from source.constants import WIDTH, HEIGHT
from source.constants.palette import BALL_COLOR, BACKGROUND_COLOR, BORDER_COLOR


class UserInterface:
    '''
    Class used to display stuff on the screen.
    '''

    def __init__(self, draw_entities):
        self.font = pg.font.Font('assets/fonts/dotty/dotty.ttf', 256)
        self.surface = pg.display.get_surface()
        self.draw_entities = draw_entities

    def draw(self):
        '''
        Draws the game.
        '''
        for place in ['middle', 'top', 'bottom', 'left', 'right']:
            if place == 'middle':
                size = 5
                pos = (WIDTH // 2, HEIGHT // 2)
                surf = pg.Surface((size, HEIGHT))
            else:
                size = 10
                if place == 'top':
                    pos = WIDTH // 2, 0
                    surf = pg.Surface((WIDTH, size))
                elif place == 'bottom':
                    pos = WIDTH // 2, HEIGHT
                    surf = pg.Surface((WIDTH, size))
                elif place == 'left':
                    pos = 0, HEIGHT // 2
                    surf = pg.Surface((size, HEIGHT))
                elif place == 'right':
                    pos = WIDTH, HEIGHT // 2
                    surf = pg.Surface((size, HEIGHT))
            surf.fill(BORDER_COLOR)
            rect = surf.get_rect(center=pos)
            self.surface.blit(surf, rect)
        self.draw_entities(self.surface)

    def pause_text(self, ball_is_moving):
        '''
        Displays pause text if the ball is not moving.
        '''
        if not ball_is_moving:
            image = self.font.render(
                'SPACE', False, BALL_COLOR, BACKGROUND_COLOR)
            rect = image.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
        else:
            image = pg.Surface((0, 0))
            rect = image.get_rect()
        self.surface.blit(image, rect)
