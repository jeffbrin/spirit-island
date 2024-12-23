from enums import LandType
from board import Land, Board
from invader_cards import InvaderCard
from entities import Explorer, Town, City

class InvaderActions():
    def __init__(self, ravage_land: InvaderCard, build_land: InvaderCard, explore_land: InvaderCard):
        self.ravage_land = ravage_land
        self.build_land = build_land
        self.explore_land = explore_land

    def ravage(self, board: Board, ravage_land: list[LandType]):
        for land in board.lands.values():
            if land.land_type in ravage_land:
                land.take_damage_from_invaders()
    
    def explore(self, board: Board, explore_card: InvaderCard):
        def neighbour_city_town(land: Land):
            for neighbor in land.neighbours:
                if len(neighbor.towns) > 0 or len(neighbor.cities) > 0:
                    return True
                else:
                    return False
                
        for land in board.lands.values():
            if  land.land_type in explore_card.land_types and (
                    land.invader_damage > 0 or \
                    land.coastal or \
                    neighbour_city_town(land)):
                land.add(Explorer())

    def build(self, board: Board, build_card: InvaderCard):
        for land in board.lands.values():
            if land.land_type in build_card.land_types and \
                    land.invader_damage > 0:
                if len(land.towns) >= len(land.cities):
                    land.add(City())
                else:
                    land.add(Town())
    
