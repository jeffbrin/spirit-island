from enums import LandType, Entities
from board import Land, Board
from .gamestate import GameState
from blight_pool import BlightPool
from invader_cards import InvaderCards
import numpy as np


class InvaderActions(GameState):
    def __init__(self, ravage_land: InvaderCards, build_land: InvaderCards, explore_Land: InvaderCards):
        self.ravage_land = ravage_land
        self.build_land = build_land
        self.explore_land = explore_Land

    def ravage(self, ravage_land):
        for land in Board.lands:
            if land.land_type in ravage_land and land.invader_damage != 0:
                # Need to add defense condition

                #removing dahans 
                nb_dead_dahans = np.floor(land.invader_damage/2).astype(int)
                for _ in range(nb_dead_dahans):
                    try:
                        land.remove(Entities.DAHAN)
                    except:
                        break
                
                #adding blight
                if land.invader_damage >= 2:
                    def add_blight(initial_land: Land) -> Land:
                        if initial_land.blights >= 1:
                            land.add(Entities.BLIGHT)
                            BlightPool.remove_to_pool()
                            try:
                                land.presences.pop()
                            except:
                                pass
                            choose_land = int(input(f'Choose land from {[i.land_ID for i in land.neighbours]} to add blight'))
                            matching = [i for i in Board.lands if i.land_ID == choose_land]
                            return add_blight(matching[0])
                        else:
                            land.add(Entities.BLIGHT)
                            BlightPool.remove_to_pool()
                            try:
                                land.presences.pop()
                            except:
                                pass
    
    def explore(self, explore_land):
        def neighbour_city_town(land: Land):
            for i in land.neighbours:
                if len(i.towns) > 0 or len(i.cities) > 0:
                    return True
                else:
                    return False
                
        for land in Board.lands:
            if  land in explore_land and (
                land.invader_damage != 0 or\
                land.coastal == True or\
                neighbour_city_town(land) == True):
                land.add(Entities.EXPLORER)

    def build(self, build_land):
        for land in Board.lands:
            if land in build_land and (len(land.towns) > 0) or (len(land.towns) > 0):
                if len(land.towns) >= len(land.cities):
                    land.add(Entities.TOWN)
                else:
                    land.add(Entities.CITY)
    

            




    
                

            
        
                

                    
                        


                    


                


                


