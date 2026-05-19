from constants import tile_size, white_color
from entities.game_object import GameObject
import pygame


class Wall(GameObject):
    def __init__(self,x,y,blok_czolg = True, blok_pocisk = True, desc = True):
        self.hitbox = pygame.Rect(x,y,tile_size,tile_size)
        super().__init__(x,y,None, self.hitbox)
        self.blok_czolg = blok_czolg
        self.blok_pocisk = blok_pocisk
        self.desc = desc

    def update(self):
        pass

    def draw(self,screen):
        if self.sprite:
            screen.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(screen,white_color,self.hitbox)