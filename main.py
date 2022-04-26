from threading import Thread
from source.controller.game import Game
from source.utils.cli import cls

if __name__ == "__main__":
    cls()
    game = Game()
    thread = Thread(target=game.increase_ball_speed)
    thread.start()
    game.run()
