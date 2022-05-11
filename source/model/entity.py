import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, groups, pos, size, base_speed, color):
        super().__init__(groups)
        self.image = pg.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)
        self._hitbox = self.rect
        self._direction = pg.math.Vector2(0, 0)
        self._base_speed = base_speed
        self._speed = self._base_speed
