from enum import Enum

class GrowthComponent(Enum):
    RECLAIM_CARDS: 0
    GAIN_POWER_CARD: 1
    PLACE_PRESENCE: 2
    GAIN_ENERGY: 3

class GrowthOption:
    def __init__(self, actions: list[tuple[GrowthComponent, int]]):
        """
        Initializes the growth option.

        Parameters
        ----------
        actions : list[tuple[GrowthComponent, int]]
            A list of actions to take as part of the growth stage. Each action is a tuple
            where the first element is the GrowthComponent and the second element is the
            numeric quantifier for that action. The second component represents different
            things depending on the type of action. For GAIN_ENERGY, it is the quantity
            of energy to gain. For PLACE_PRESENCE, it is the distance from existing 
            presence that another presence can be placed.
        """
        self.actions = actions