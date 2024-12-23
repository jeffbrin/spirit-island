from .entity import Entity

class Invader(Entity):
    def __init__(self, damage: int, health: int, fear_generation: int):
        super(Invader, self).__init__(damage, health)
        self.fear_generation = fear_generation

class Explorer(Invader):
    DAMAGE = 1
    HEALTH = 1
    FEAR_GENERATION = 0

    def __init__(self):
        super().__init__(Explorer.DAMAGE, Explorer.HEALTH, Explorer.FEAR_GENERATION)

class Town(Invader):
    DAMAGE = 2
    HEALTH = 2
    FEAR_GENERATION = 1

    def __init__(self):
        super().__init__(Town.DAMAGE, Town.HEALTH, Town.FEAR_GENERATION)

class City(Invader):
    DAMAGE = 3
    HEALTH = 3
    FEAR_GENERATION = 2

    def __init__(self):
        super().__init__(City.DAMAGE, City.HEALTH, City.FEAR_GENERATION)
