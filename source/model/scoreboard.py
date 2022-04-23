import pygame as pg
from source.model.paddle import Paddle
from source.utils.palette import P1_COLOR, P2_COLOR
from source.utils.settings import WIDTH, HEIGHT


class Scoreboard(pg.sprite.Sprite):
    def __init__(self, categories: pg.sprite.Group | list, paddle: Paddle):
        super().__init__(categories)
        self.paddle = paddle
        self.font = pg.font.Font("assets/fonts/dotty/dotty.ttf", 256)
        self.__set_side__()

    def __set_side__(self):
        if self.paddle.get_side() == "left":
            self.pos = WIDTH // 4, HEIGHT // 2
            self.color = P1_COLOR
        elif self.paddle.get_side() == "right":
            self.pos = WIDTH * 3 // 4, HEIGHT // 2
            self.color = P2_COLOR

    def update(self):
        self.image = self.font.render(self.paddle.get_score(), False,
                                      self.color)
        self.rect = self.image.get_rect(center=self.pos)
