'''
Main file of the program.
'''
from threading import Thread, Event
import sys
import pygame as pg
from source.constants import FPS, RESOLUTION, TITLE
from source.constants.palette import BACKGROUND_COLOR
from source.ui import UserInterface
from source.ui.cli import cmd_clear
from source.sprites import Ball, Paddle


class Game:
    '''
    Class to control most of the game state.
    '''

    def __init__(self):
        pg.init()
        # Window
        self.window = pg.display.set_mode(RESOLUTION)
        pg.display.set_caption(TITLE)
        icon = pg.image.load('assets/images/game-icon.png')
        pg.display.set_icon(icon)
        # Clock
        self.clock = pg.time.Clock()
        # Groups
        self.entities = pg.sprite.Group()
        # Entities
        player_1 = Paddle(self.entities, 'left')
        player_2 = Paddle(self.entities, 'right')
        self.ball = Ball(self.entities, [player_1, player_2])
        # Info
        self.user_interface = UserInterface(self.entities.draw)
        # Threads
        self.event = Event()
        self.thread = Thread(target=self.increase_ball_speed)
        # BGM
        pg.mixer.music.load('assets/music/Beep_beat_by-feels_B._loop.wav')
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play(-1)

    def run(self):
        '''
        Main game loop.
        '''
        self.thread.start()
        while True:
            self.clock.tick(FPS)
            self.__events()
            self.__update()
            self.__draw()

    def __events(self):
        for event in pg.event.get():
            keys = pg.key.get_pressed()
            if event.type == pg.QUIT or keys[pg.K_ESCAPE]:
                self.event.set()
                print('GAME OVER!\n')
                sys.exit()

    def __update(self):
        self.entities.update()

    def __draw(self):
        self.window.fill(BACKGROUND_COLOR)
        self.user_interface.draw()
        self.user_interface.pause_text(self.ball.is_moving())
        pg.display.flip()

    def increase_ball_speed(self):
        '''
        Increase the speed of the ball.
        '''
        while not self.event.is_set():
            if self.ball.is_moving():
                self.event.wait(5)
                self.ball.increase_speed()


if __name__ == '__main__':
    cmd_clear()
    game = Game()
    game.run()
