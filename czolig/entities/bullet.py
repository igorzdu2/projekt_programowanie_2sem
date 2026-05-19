import pygame

from constants import bullet_size, bullet_color
from entities.game_object import GameObject

class Bullet(GameObject):
    def __init__(self, x, y,kierunek):
        maly_hitbox = pygame.Rect(x, y, bullet_size, bullet_size)
        super().__init__(x,y,None,maly_hitbox)
        self.kierunek = kierunek
        self.speed = 8

    def update(self):
        if self.kierunek=="UP":
            self.y -= self.speed
        elif self.kierunek=="DOWN":
            self.y += self.speed
        elif self.kierunek=="LEFT":
            self.x -= self.speed
        elif self.kierunek=="RIGHT":
            self.x += self.speed

        self.hitbox.x = self.x
        self.hitbox.y = self.y

    def draw(self,screen):
        if self.sprite:
            screen.blit(self.sprite, (self.x, self.y))
        else:
            pygame.draw.rect(screen,bullet_color,self.hitbox)


