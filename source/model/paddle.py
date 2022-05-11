import pygame as pg
from source.model.entity import Entity
from source.model.score import Score
from source.utils.palette import P1_COLOR, P2_COLOR
from source.utils.settings import WIDTH, HEIGHT


class Paddle(Entity):
    def __init__(self, groups, side):
        if not side in ["left", "right"]:
            raise ValueError("Side must be 'left' or 'right'!")
        else:
            pos = (30, HEIGHT // 2) if side == "left" else (WIDTH - 30, HEIGHT // 2)
            size = 10, 120
            _base_speed = 4
            color = P1_COLOR if side == "left" else P2_COLOR
            super().__init__(groups, pos, size, _base_speed, color)
            self.__side = side
            self.__score = Score(groups, side)

    def update(self):
        self.__input()
        self.__move()

    def __input(self):
        keys = pg.key.get_pressed()
        if self.__side == "left":
            if keys[pg.K_w]:
                self._direction.y = -1
            elif keys[pg.K_s]:
                self._direction.y = 1
            else:
                self._direction.y = 0
        elif self.__side == "right":
            if keys[pg.K_UP]:
                self._direction.y = -1
            elif keys[pg.K_DOWN]:
                self._direction.y = 1
            else:
                self._direction.y = 0

    def __move(self):
        self._hitbox.y += self._direction.y * self._speed
        self.__handle_collisions()
        self.rect.center = self._hitbox.center

    def __handle_collisions(self):
        if self._direction.y == -1 and self.rect.top <= 0:
            self._hitbox.top = 0
        elif self._direction.y == 1 and self.rect.bottom >= HEIGHT:
            self._hitbox.bottom = HEIGHT

    def increase_score(self):
        self.__score.increase()

    def get_side(self):
        return self.__side
