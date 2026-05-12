import pygame
import sys

class Environment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Tanks 1990")
        self.zegar = pygame.time.Clock()
        self.dzialanie = True

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.dzialanie = False




    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        pygame.display.flip()

    def run(self):
        while self.dzialanie:
            self.events()
            self.update()
            self.draw()
            self.zegar.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Environment()
    game.run()