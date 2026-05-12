from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x,y,sprite,hitbox):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.hitbox = hitbox

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self,screen):
        pass