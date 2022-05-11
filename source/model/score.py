import pygame as pg
from source.utils.palette import P1_COLOR, P2_COLOR
from source.utils.settings import WIDTH, HEIGHT


class Score(pg.sprite.Sprite):
    def __init__(self, groups, paddle_side):
        super().__init__(groups)
        self.__font = pg.font.Font("assets/fonts/dotty/dotty.ttf", 256)
        self.__total = 0
        self.__placement(paddle_side)

    def __placement(self, paddle_side):
        if paddle_side == "left":
            self.__pos = WIDTH // 4, HEIGHT // 2
            self.__color = P1_COLOR
        elif paddle_side == "right":
            self.__pos = WIDTH * 3 // 4, HEIGHT // 2
            self.__color = P2_COLOR

    def update(self):
        self.image = self.__font.render(str(self.__total), False, self.__color)
        self.rect = self.image.get_rect(center=self.__pos)

    def increase(self):
        self.__total += 1
