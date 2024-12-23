from enums import LandType, Entities
from board import Land, Board
from .gamestate import GameState
from blight_pool import BlightPool
from invader_cards import InvaderCard


class InvaderActions(GameState):
    def __init__(self, ravage_land: InvaderCard, build_land: InvaderCard, explore_land: InvaderCard):
        self.ravage_land = ravage_land
        self.build_land = build_land
        self.explore_land = explore_land

    def ravage(self, ravage_land: list[LandType]):
        for land in Board.lands:
            if land.land_type in ravage_land:
                land.take_damage_from_invaders()
    
    def explore(self, explore_land: InvaderCard):
        def neighbour_city_town(land: Land):
            for i in land.neighbours:
                if len(i.towns) > 0 or len(i.cities) > 0:
                    return True
                else:
                    return False
                
        for land in Board.lands:
            # TODO: Fix land in explore_land
            # since explore_land is not a list of lands
            if  land in explore_land and (
                land.invader_damage != 0 or\
                land.coastal == True or\
                neighbour_city_town(land) == True):
                land.add(Entities.EXPLORER)

    def build(self, build_land):
        for land in Board.lands:
            if land in build_land and (len(land.towns) > 0) or (len(land.towns) > 0):
                if len(land.towns) >= len(land.cities):
                    land.add(Entities.CITY)
                else:
                    land.add(Entities.TOWN)
    
