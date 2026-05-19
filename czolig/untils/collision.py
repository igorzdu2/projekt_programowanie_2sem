import pygame
from constants import szer_ekranu,wys_ekranu

def kolizja_gracz_sciana(gracz,lista):
    for w in lista:
        if gracz.hitbox.colliderect(w.hitbox):
            if gracz.kierunek == "UP":
                gracz.y += gracz.speed
            if gracz.kierunek == "DOWN":
                gracz.y -= gracz.speed
            if gracz.kierunek == "LEFT":
                gracz.x += gracz.speed
            if gracz.kierunek == "RIGHT":
                gracz.x -= gracz.speed

            gracz.hitbox.x = gracz.x
            gracz.hitbox.y = gracz.y

def kolizja_pocisk_sciana(pociski,lista):
    for p in pociski[:]:
        p.update()
        for m in lista[:]:
            if p.hitbox.colliderect(m.hitbox):
                lista.remove(m)
                pociski.remove(p)
                break
        if p.x < 0 or p.x > szer_ekranu or p.y < 0 or p.y > wys_ekranu:
            if p in pociski:
                pociski.remove(p)