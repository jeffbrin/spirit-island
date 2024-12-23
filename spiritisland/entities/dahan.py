from . import Entity

class Dahan(Entity):
    DAMAGE = 2
    HEALTH = 2

    def __init__(self):
        super().__init__(Dahan.DAMAGE, Dahan.HEALTH)
