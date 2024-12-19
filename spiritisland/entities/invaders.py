from .entity import Entity
from  board import Land

class Invader(Entity):
    pass

class Explorer(Invader):
    def __init__(self):
        self.damage = 1,
        self.heatlh = 1

class Town(Invader):
    def __init__(self):
        self.damage = 2,
        self.heatlh = 2
    pass

class City(Invader):
    def __init__(self):
        self.damage = 3,
        self.heatlh = 3
    pass
