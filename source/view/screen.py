import pygame as pg
from source.utils.settings import WIDTH, HEIGHT
from source.utils.palette import BALL_COLOR, BG_COLOR, BORDER_COLOR


class Screen:
    def __init__(self, __entities):
        self.__surface = pg.display.get_surface()
        self.__entities = __entities

    def draw(self):
        self.__draw_borders()
        self.__entities.draw(self.__surface)

    def update(self):
        self.__entities.update()

    def __draw_borders(self):
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
            self.__surface.blit(surf, rect)

    def pause_text(self, ball_is_moving):
        if not ball_is_moving:
            font = pg.font.Font("assets/fonts/dotty/dotty.ttf", 256)
            image = font.render("SPACE", False, BALL_COLOR, BG_COLOR)
            rect = image.get_rect(center=(WIDTH // 2, HEIGHT * 3 // 4))
        else:
            image = pg.Surface((0, 0))
            rect = image.get_rect()
        self.__surface.blit(image, rect)
