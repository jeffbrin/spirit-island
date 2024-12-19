from board import Land
from entities import Entity, Dahan, Explorer, Town, City, Presence, Blight
from enums import LandType, Entities
class Board():
    def __init__(self):
        self.lands = []
    
    def choose_board():
        board = input(f'Choose Board from A, B, C, D: ').upper()
        while board not in {'A', 'B', 'C', 'D'}:
            print(f'Board {board} was not in options')
            return choose_board()
        
        def enter_neighbours(initial_land, neighbours: list):
                for i in neighbours:
                    board_list.get(initial_land).add_neighbour(board_list.get(i))

        if board == 'A':
            board_list = {
                'land1' : Land(land_type = LandType.MOUNTAIN, land_ID = 1, coastal = True),
                'land2' : Land(land_type = LandType.WETLAND, land_ID = 2, coastal = True),
                'land3' : Land(land_type = LandType.GRASSLAND, land_ID = 3, coastal = True),
                'land4' : Land(land_type = LandType.SAND, land_ID = 4, coastal = False),
                'land5' : Land(land_type = LandType.WETLAND, land_ID = 5, coastal = False),
                'land6' : Land(land_type = LandType.MOUNTAIN, land_ID = 6, coastal = False),
                'land7' : Land(land_type = LandType.SAND, land_ID = 7, coastal = False),
                'land8' : Land(land_type = LandType.GRASSLAND, land_ID = 8, coastal = False)
            }

            for i in board_list.values():
                Board.lands.append(i)
            
            enter_neighbours('land1', ['land2', 'land4', 'land5','land6'])
            enter_neighbours('land2', ['land1', 'land3', 'land4'])
            enter_neighbours('land3', ['land2', 'land4'])
            enter_neighbours('land4', ['land1', 'land2', 'land3', 'land5'])
            enter_neighbours('land5', ['land1', 'land4', 'land6', 'land7', 'land8'])
            enter_neighbours('land6', ['land1', 'land5', 'land8'])
            enter_neighbours('land7', ['land5', 'land8'])
            enter_neighbours('land8', ['land5', 'land6', 'land7'])
            
        elif board == 'B':
            board_list = {
                'land1' : Land(land_type = LandType.WETLAND, land_ID = 1, coastal = True),
                'land2' : Land(land_type = LandType.MOUNTAIN, land_ID = 2, coastal = True),
                'land3' : Land(land_type = LandType.SAND, land_ID = 3, coastal = True),
                'land4' : Land(land_type = LandType.GRASSLAND, land_ID = 4, coastal = False),
                'land5' : Land(land_type = LandType.SAND, land_ID = 5, coastal = False),
                'land6' : Land(land_type = LandType.WETLAND, land_ID = 6, coastal = False),
                'land7' : Land(land_type = LandType.MOUNTAIN, land_ID = 7, coastal = False),
                'land8' : Land(land_type = LandType.GRASSLAND, land_ID = 8, coastal = False)
            }

            for i in board_list.values():
                Board.lands.append(i)
            
            enter_neighbours('land1', ['land2', 'land4', 'land5', 'land6'])
            enter_neighbours('land2', ['land1', 'land3', 'land4'])
            enter_neighbours('land3', ['land2', 'land4'])
            enter_neighbours('land4', ['land1', 'land2', 'land3', 'land5', 'land7'])
            enter_neighbours('land5', ['land1', 'land4', 'land6', 'land7'])
            enter_neighbours('land6', ['land1', 'land5', 'land7', 'land8'])
            enter_neighbours('land7', ['land4', 'land5', 'land6', 'land8'])
            enter_neighbours('land8', ['land6', 'land7'])
        
        elif board == 'C':
            board_list = {
                'land1' : Land(land_type = LandType.GRASSLAND, land_ID = 1, coastal = True),
                'land2' : Land(land_type = LandType.SAND, land_ID = 2, coastal = True),
                'land3' : Land(land_type = LandType.MOUNTAIN, land_ID = 3, coastal = True),
                'land4' : Land(land_type = LandType.GRASSLAND, land_ID = 4, coastal = False),
                'land5' : Land(land_type = LandType.WETLAND, land_ID = 5, coastal = False),
                'land6' : Land(land_type = LandType.SAND, land_ID = 6, coastal = False),
                'land7' : Land(land_type = LandType.MOUNTAIN, land_ID = 7, coastal = False),
                'land8' : Land(land_type = LandType.WETLAND, land_ID = 8, coastal = False)
            }

            for i in board_list.values():
                Board.lands.append(i)
            
            enter_neighbours('land1', ['land2', 'land5', 'land6'])
            enter_neighbours('land2', ['land1', 'land3', 'land4', 'land5'])
            enter_neighbours('land3', ['land2', 'land4'])
            enter_neighbours('land4', ['land2', 'land3', 'land5', 'land7'])
            enter_neighbours('land5', ['land1', 'land2', 'land4', 'land6', 'land7'])
            enter_neighbours('land6', ['land1', 'land5', 'land7', 'land8'])
            enter_neighbours('land7', ['land4', 'land5', 'land6', 'land8'])
            enter_neighbours('land8', ['land6', 'land7'])
        
        elif board == 'D':
            board_list = {
                'land1' : Land(land_type = LandType.WETLAND, land_ID = 1, coastal = True),
                'land2' : Land(land_type = LandType.GRASSLAND, land_ID = 2, coastal = True),
                'land3' : Land(land_type = LandType.WETLAND, land_ID = 3, coastal = True),
                'land4' : Land(land_type = LandType.SAND, land_ID = 4, coastal = False),
                'land5' : Land(land_type = LandType.MOUNTAIN, land_ID = 5, coastal = False),
                'land6' : Land(land_type = LandType.GRASSLAND, land_ID = 6, coastal = False),
                'land7' : Land(land_type = LandType.SAND, land_ID = 7, coastal = False),
                'land8' : Land(land_type = LandType.MOUNTAIN, land_ID = 8, coastal = False)
            }

            for i in board_list.values():
                Board.lands.append(i)
            
            enter_neighbours('land1', ['land2', 'land5', 'land7', 'land8'])
            enter_neighbours('land2', ['land1', 'land3', 'land4', 'land5'])
            enter_neighbours('land3', ['land2', 'land4'])
            enter_neighbours('land4', ['land2', 'land3', 'land5', 'land6'])
            enter_neighbours('land5', ['land1', 'land2', 'land3', 'land4', 'land6', 'land7'])
            enter_neighbours('land6', ['land4', 'land5', 'land7'])
            enter_neighbours('land7', ['land1', 'land5', 'land6', 'land8'])
            enter_neighbours('land8', ['land1', 'land7'])
        
        
        
            
        