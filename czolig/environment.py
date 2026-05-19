import pygame
import sys
from entities.player_tank import PlayerTank
from entities.Walls.wall import Wall
from constants import *
from untils.collision import kolizja_gracz_sciana, kolizja_pocisk_sciana


class Environment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((szer_ekranu, wys_ekranu))
        pygame.display.set_caption("Tanks 1990")
        self.zegar = pygame.time.Clock()
        self.dzialanie = True
        hitbox1 = pygame.Rect(400,300,tile_size,tile_size)
        self.gracz = PlayerTank(100,200,None,hitbox1,100,2,1)
        self.pociski = []
        self.mury = []
        self.mury.append(Wall(400,300))
        self.mury.append(Wall(500,200))

    def events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.dzialanie = False


    def update(self):

        zlapany = self.gracz.update()
        if zlapany:
            self.pociski.append(zlapany)

        kolizja_gracz_sciana(self.gracz, self.mury)
        kolizja_pocisk_sciana(self.pociski, self.mury)

    def draw(self):
        self.screen.fill(black_color)
        self.gracz.draw(self.screen)
        for m in self.mury:
            m.draw(self.screen)
        for p in self.pociski:
            p.draw(self.screen)
        pygame.display.flip()



    def run(self):
        while self.dzialanie:
            self.events()
            self.update()
            self.draw()
            self.zegar.tick(fps)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Environment()
    game.run()