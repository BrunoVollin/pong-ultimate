import pygame as pg
from source.model.entity import Entity
from source.utils.palette import P1_COLOR, P2_COLOR
from source.utils.settings import WIDTH, HEIGHT


class Paddle(Entity):
    def __init__(self, categories: pg.sprite.Group | list, side: str):
        if not side in ["left", "right"]:
            raise ValueError("Side must be 'left' or 'right'!")
        pos = (30, HEIGHT // 2) if side == "left" else (WIDTH - 30, HEIGHT // 2)
        color = P1_COLOR if side == "left" else P2_COLOR
        super().__init__(categories, pos, (10, 120), 4, color)
        self.side = side
        self.score = 0

    def update(self):
        self.__input__()
        self.__move__()

    def __input__(self):
        keys = pg.key.get_pressed()
        if self.side == "left":
            if keys[pg.K_w]:
                self.direction.y = -1
            elif keys[pg.K_s]:
                self.direction.y = 1
            else:
                self.direction.y = 0
        elif self.side == "right":
            if keys[pg.K_UP]:
                self.direction.y = -1
            elif keys[pg.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.y = 0

    def __move__(self):
        self.hitbox.y += self.direction.y * self.speed
        self.__threat_collisions__()
        self.rect.center = self.hitbox.center

    def __threat_collisions__(self):
        if self.direction.y == -1 and self.rect.top <= 0:
            self.hitbox.top = 0
        elif self.direction.y == 1 and self.rect.bottom >= HEIGHT:
            self.hitbox.bottom = HEIGHT

    def increase_score(self):
        self.score += 1

    def get_side(self):
        return self.side

    def get_score(self):
        return str(self.score)
