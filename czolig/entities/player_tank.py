from constants import szer_ekranu, tile_size, wys_ekranu, bullet_size, player_color
from entities.tank import Tank
import pygame
from entities.bullet import Bullet

class PlayerTank(Tank):
    def __init__(self,x,y,sprite,hitbox,hp,lives,speed):
        super().__init__(x,y,sprite,hitbox,hp,lives,speed)


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
            self.kierunek = "UP"
        elif keys[pygame.K_s]:
            self.y += self.speed
            self.kierunek = "DOWN"
        elif keys[pygame.K_a]:
            self.x -= self.speed
            self.kierunek = "LEFT"
        elif keys[pygame.K_d]:
            self.x += self.speed
            self.kierunek = "RIGHT"

        if self.x < 0:
            self.x = 0
        if self.x > szer_ekranu-tile_size:
            self.x = szer_ekranu-tile_size
        if self.y < 0:
            self.y = 0
        if self.y > wys_ekranu-tile_size:
            self.y = wys_ekranu - tile_size

        self.hitbox.x = self.x
        self.hitbox.y = self.y

        if self.cooldown > 0:
            self.cooldown -= 1

        if keys[pygame.K_SPACE] and self.cooldown == 0:
            print("Wystrial")
            self.cooldown = 30
            pocisk = Bullet(self.x+(tile_size/2-bullet_size/2),self.y+(tile_size/2-bullet_size/2),self.kierunek)
            return pocisk

        return None

    def draw(self,screen):
        if self.sprite:
            screen.blit(self.sprite,(self.x,self.y))
        else:
            pygame.draw.rect(screen,player_color,self.hitbox)




