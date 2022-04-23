import pygame as pg
from source.utils.settings import WIDTH, HEIGHT
from source.utils.palette import BG_COLOR, BORDER_COLOR


class Screen(object):
    def __init__(self, info: pg.sprite.Group, entities: pg.sprite.Group):
        self.display = pg.display.get_surface()
        pg.display.set_caption("Pong")
        self.clock = pg.time.Clock()
        self.info = info
        self.entities = entities
        self.info.update()

    def draw(self):
        self.__draw_borders__()
        self.info.draw(self.display)
        self.entities.draw(self.display)

    def update(self):
        self.info.update()
        self.entities.update()

    def __draw_borders__(self):
        for place in ["middle", "top", "bottom", "left", "right"]:
            if place == "middle":
                size = 5
                pos = (WIDTH // 2, HEIGHT // 2)
                surf = pg.Surface((size, HEIGHT))
            else:
                size = 10
                if place == "top":
                    pos = WIDTH // 2, 0
                    surf = pg.Surface((WIDTH, size))
                elif place == "bottom":
                    pos = WIDTH // 2, HEIGHT
                    surf = pg.Surface((WIDTH, size))
                elif place == "left":
                    pos = 0, HEIGHT // 2
                    surf = pg.Surface((size, HEIGHT))
                elif place == "right":
                    pos = WIDTH, HEIGHT // 2
                    surf = pg.Surface((size, HEIGHT))
            surf.fill(BORDER_COLOR)
            rect = surf.get_rect(center=pos)
            self.display.blit(surf, rect)
