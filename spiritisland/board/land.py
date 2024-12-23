from enums import LandType, Entities
from entities import Entity, Dahan, Explorer, Town, City, Presence, Blight
from gamestate import BlightPool


class Land:
    def __init__(
            self,
            land_type: LandType,
            land_ID: int,
            dahans: int = 0,
            explorers: int = 0,
            towns: int = 0,
            cities: int = 0,
            blight: int = 0,
            presences: int = 0,
            coastal: bool = False,
            ):
        
        self.land_type = land_type
        self.id = land_ID
        self.coastal = coastal
        self.dahans = []
        self.explorers = []
        self.towns = []
        self.cities = []
        self.presences = []
        self.blight = []
        self.neighbours = []
        

        for _ in range(dahans):
            self.add(Dahan())
        for _ in range(explorers):
            self.add(Explorer())
        for _ in range(towns):
            self.add(Town())
        for _ in range(cities):
            self.add(City())
        for _ in range(presences):
            self.add(Presence())
        for _ in range(blight):
            self.add(Blight())

    @property
    def invader_damage(self) -> int:
        return len(self.explorers)*Explorer.damage + len(self.towns)*Town.damage + len(self.cities)*City.damage

    def add(self, entity: Entity):
        if isinstance(entity, Dahan):
            self.dahans.append(entity)
        elif isinstance(entity, Explorer):
            self.explorers.append(entity)
        elif isinstance(entity, Town):
            self.towns.append(entity)
        elif isinstance(entity, City):
            self.cities.append(entity)
        elif isinstance(entity, Presence):
            self.presences.append(entity)
        elif isinstance(entity, Blight):
            self.blight.append(entity)
        else:
            raise TypeError(f'{type(entity)} is not a valid type.')
       
    def remove(self, entity_code: Entities) -> Entity:
        try: 
            if entity_code == Entities.DAHAN:
                return self.dahans.pop()
            if entity_code == Entities.EXPLORER:
                return self.explorers.pop()
            if entity_code == Entities.TOWN:
                return self.towns.pop()
            if entity_code == Entities.CITY:
                return self.cities.pop()
            if entity_code == Entities.PRESENCE:
                return self.presences.pop()
            if entity_code == Entities.BLIGHT:
                return self.blight.pop()
            else:
                raise TypeError(f'{entity_code.name.title()} is not a valid Entity.')
        except IndexError:
            raise TypeError(f'Tried to pop from list: {entity_code.name.title()} but was empty.')
    
    def add_neighbour(self, neighbour: "Land"):
        self.neighbours.append(neighbour)
    
    def available_target_lands(self, distance: int) -> list:
        def add_lands(previous_list):
            temp = [i for i in previous_list]
            for i in previous_list:
                for j in i.neighbours:
                    if j not in temp:
                        temp.append(j)
            return temp
        
        result = [self]
        for _ in range(distance):
            result = add_lands(result)
        return result
    
    def take_damage_from_invaders(self, blight_pool: BlightPool) -> None:
        # TODO: Add Defense Stuff

        #removing dahans 
        nb_dead_dahans = int(self.invader_damage / 2)
        for _ in range(nb_dead_dahans):
            self.remove(Entities.DAHAN)

        if self.invader_damage >= 2:
            return self.add_blight(blight_pool)
        
        return False
    
    def add_blight(self, blight_pool: BlightPool) -> bool:
        """
        Adds blight to the land, returns True if another blight has to be added to a neighbouring land.
        """

        self.add(Blight())
        blight_pool.remove()
        self.remove(Entities.PRESENCE)
        return len(self.blight) > 1
