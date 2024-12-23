from enums import LandType

class InvaderCard():
    def __init__(self, land_types: list[LandType], fear_phase: int):
        self.fear_phase = fear_phase
        self.land_types = land_types