from entities.game_object import GameObject


class Tank(GameObject):
    def __init__(self,x,y,sprite,hitbox,hp,lives,speed):
        super().__init__(x,y,sprite,hitbox)
        self.lives = lives
        self.hp = hp
        self.speed = speed
        self.kierunek = "UP"
        self.level = 1
        self.cooldown = 0

    def update(self):
        pass
    def draw(self,screen):
        pass
