import pygame as pg
from source.utils.palette import BALL_COLOR, BG_COLOR
from source.utils.settings import WIDTH, HEIGHT


class PauseText(pg.sprite.Sprite):
    def __init__(self, categories, ball):
        super().__init__(categories)
        self.ball = ball
        self.font = pg.font.Font("assets/fonts/dotty/dotty.ttf", 256)
        self.pos = WIDTH // 2, HEIGHT * 3 // 4

    def update(self):
        if self.ball.is_moving(False):
            self.image = self.font.render("SPACE", False, BALL_COLOR, BG_COLOR)
            self.rect = self.image.get_rect(center=self.pos)
        else:
            self.image = pg.Surface((0, 0))
            self.rect = self.image.get_rect()
