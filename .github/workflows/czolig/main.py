from environment import Environment
from game_object import GameObject


if __name__ == "__main__":
    game = Environment()
    test = GameObject(0,0,None, None)
    game.run()
