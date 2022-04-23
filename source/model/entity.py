import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, categories: pg.sprite.Group | list, pos: tuple,
                 size: tuple, base_speed: int, color: str):
        super().__init__(categories)
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self.hitbox = self.rect
        self.direction = pg.math.Vector2(0, 0)
        self.base_speed = base_speed
        self.speed = self.base_speed
