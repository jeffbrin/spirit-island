from enums import LandType
from board import Land, Board
from invader_cards import InvaderCard
from entities import Explorer, Town, City

class InvaderBoard():
    def __init__(self):
        # TODO: Make list of land types
        self.cards = [InvaderCard(land_types, fear_phase) for land_types, fear_phase in zip(
            ([LandType.SAND], [LandType.MOUNTAIN], [LandType.WETLAND], [LandType.GRASSLAND], [LandType.SAND], [LandType.COASTAL], [LandType.MOUNTAIN, LandType.GRASSLAND], [LandType.MOUNTAIN, LandType.WETLAND], [LandType.SAND, LandType.GRASSLAND])
            (1, 1, 1, 2, 2, 2, 3, 3, 3)
        )]
        self.explore_card = None
        self.build_card = None
        self.ravage_card = None

    def ravage(self, board: Board):
        if self.ravage_card is None:
            return
        
        for land in board.lands.values():
            if land.land_type in self.ravage_land:
                land.take_damage_from_invaders()
    
    def explore(self, board: Board):
        if self.explore_card is None:
            return

        def has_neighbouring_building(land: Land):
            for neighbor in land.neighbours:
                if len(neighbor.towns) > 0 or len(neighbor.cities) > 0:
                    return True
                else:
                    return False
                
        for land in board.lands.values():
            if  land.land_type in self.explore_card.land_types and (
                    land.invader_damage > 0 or \
                    land.coastal or \
                    has_neighbouring_building(land)):
                land.add(Explorer())

    def build(self, board: Board):
        if self.build_card is None:
            return False
        
        for land in board.lands.values():
            if land.land_type in self.build_card.land_types and \
                    land.invader_damage > 0:
                if len(land.towns) >= len(land.cities):
                    land.add(City())
                else:
                    land.add(Town())
    
    def progress_cards(self) -> None:
        self.ravage_card = self.build_card
        self.build_card = self.explore_card
        self.explore_card = self.cards.pop()
