import pygame as pg
import sys
from threading import Event
from source.model.ball import Ball
from source.model.paddle import Paddle
from source.utils.palette import BG_COLOR
from source.utils.settings import FPS, RESOLUTION
from source.view.screen import Screen


class Game:
    def __init__(self):
        pg.init()
        # Window
        self.__window = pg.display.set_mode(RESOLUTION)
        pg.display.set_caption("Pong Ultimate")
        icon_path = "assets/images/game-icon.png"
        icon = pg.image.load(icon_path)
        pg.display.set_icon(icon)
        # Clock
        self.__clock = pg.time.Clock()
        # Groups
        self.__entities = pg.sprite.Group()
        # Entities
        self.__p1 = Paddle(self.__entities, "left")
        self.__p2 = Paddle(self.__entities, "right")
        self.__ball = Ball(self.__entities, [self.__p1, self.__p2])
        # Info
        self.__screen = Screen(self.__entities)
        # Threads
        self.__event = Event()
        # BGM
        bgm_path = "assets/music/Beep_beat_by-feels_B._loop.wav"
        bgm = pg.mixer.Sound(bgm_path)
        bgm.play(-1)
        bgm.set_volume(0.2)

    def run(self):
        while True:
            self.__clock.tick(FPS)
            self._events()
            self._update()
            self._draw()

    def _events(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.__event.set()
                print("GAME OVER!\n")
                sys.exit()

    def _update(self):
        self.__screen.update()

    def _draw(self):
        self.__window.fill(BG_COLOR)
        self.__screen.draw()
        self.__screen.pause_text(self.__ball.is_moving())
        pg.display.flip()

    def increase_ball_speed(self):
        while not self.__event.isSet():
            if self.__ball.is_moving():
                self.__event.wait(5)
                self.__ball.increase_speed()
