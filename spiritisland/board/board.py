from . import Land
from enums import LandType
class Board():

    BOARDS_DATA = {
            'A': {
                'lands':{
                        1 : {'land_type': LandType.MOUNTAIN, 'land_ID': 1, 'coastal': True},
                        2 : {'land_type': LandType.WETLAND, 'land_ID': 2, 'coastal': True},
                        3 : {'land_type': LandType.GRASSLAND, 'land_ID': 3, 'coastal': True},
                        4 : {'land_type': LandType.SAND, 'land_ID': 4, 'coastal': False},
                        5 : {'land_type': LandType.WETLAND, 'land_ID': 5, 'coastal': False},
                        6 : {'land_type': LandType.MOUNTAIN, 'land_ID': 6, 'coastal': False},
                        7 : {'land_type': LandType.SAND, 'land_ID': 7, 'coastal': False},
                        8 : {'land_type': LandType.GRASSLAND, 'land_ID': 8, 'coastal': False}
                    },
                    'neighbors': {
                        1: (2, 4, 5,6),
                        2: (1, 3, 4),
                        3: (2, 4),
                        4: (1, 2, 3, 5),
                        5: (1, 4, 6, 7, 8),
                        6: (1, 5, 8),
                        7: (5, 8),
                        8: (5, 6, 7)
                    }
            },
            'B': {
                'lands': {
                    1 : {'land_type': LandType.WETLAND, 'land_ID': 1, 'coastal': True},
                    2 : {'land_type': LandType.MOUNTAIN, 'land_ID': 2, 'coastal': True},
                    3 : {'land_type': LandType.SAND, 'land_ID': 3, 'coastal': True},
                    4 : {'land_type': LandType.GRASSLAND, 'land_ID': 4, 'coastal': False},
                    5 : {'land_type': LandType.SAND, 'land_ID': 5, 'coastal': False},
                    6 : {'land_type': LandType.WETLAND, 'land_ID': 6, 'coastal': False},
                    7 : {'land_type': LandType.MOUNTAIN, 'land_ID': 7, 'coastal': False},
                    8 : {'land_type': LandType.GRASSLAND, 'land_ID': 8, 'coastal': False}
                },
                'neighbors': {
                    1: (2, 4, 5, 6),
                    2: (1, 3, 4),
                    3: (2, 4),
                    4: (1, 2, 3, 5, 7),
                    5: (1, 4, 6, 7),
                    6: (1, 5, 7, 8),
                    7: (4, 5, 6, 8),
                    8: (6, 7)
                }
            },
            'C': {
                'lands': {
                    1 : {'land_type': LandType.GRASSLAND, 'land_ID': 1, 'coastal': True},
                    2 : {'land_type': LandType.SAND, 'land_ID': 2, 'coastal': True},
                    3 : {'land_type': LandType.MOUNTAIN, 'land_ID': 3, 'coastal': True},
                    4 : {'land_type': LandType.GRASSLAND, 'land_ID': 4, 'coastal': False},
                    5 : {'land_type': LandType.WETLAND, 'land_ID': 5, 'coastal': False},
                    6 : {'land_type': LandType.SAND, 'land_ID': 6, 'coastal': False},
                    7 : {'land_type': LandType.MOUNTAIN, 'land_ID': 7, 'coastal': False},
                    8 : {'land_type': LandType.WETLAND, 'land_ID': 8, 'coastal': False}
                },
                'neighbors': {
                    1: (2, 5, 6),
                    2: (1, 3, 4, 5),
                    3: (2, 4),
                    4: (2, 3, 5, 7),
                    5: (1, 2, 4, 6, 7),
                    6: (1, 5, 7, 8),
                    7: (4, 5, 6, 8),
                    8: (6, 7)
                }
            },
            'D': {
                'lands': {
                    1 : {'land_type': LandType.WETLAND, 'land_ID': 1, 'coastal': True},
                    2 : {'land_type': LandType.GRASSLAND, 'land_ID': 2, 'coastal': True},
                    3 : {'land_type': LandType.WETLAND, 'land_ID': 3, 'coastal': True},
                    4 : {'land_type': LandType.SAND, 'land_ID': 4, 'coastal': False},
                    5 : {'land_type': LandType.MOUNTAIN, 'land_ID': 5, 'coastal': False},
                    6 : {'land_type': LandType.GRASSLAND, 'land_ID': 6, 'coastal': False},
                    7 : {'land_type': LandType.SAND, 'land_ID': 7, 'coastal': False},
                    8 : {'land_type': LandType.MOUNTAIN, 'land_ID': 8, 'coastal': False}
                },
                'neighbors': {
                    1: (2, 5, 7, 8),
                    2: (1, 3, 4, 5),
                    3: (2, 4),
                    4: (2, 3, 5, 6),
                    5: (1, 2, 3, 4, 6, 7),
                    6: (4, 5, 7),
                    7: (1, 5, 6, 8),
                    8: (1, 7)
                }
            }
        }

    def __init__(self):
        self.lands: dict[int, Land] = {}

    @classmethod
    def choose_board(cls, choice: str) -> "Board":

        board = cls()
        try:
            board_data = cls.BOARDS_DATA[choice]
        except KeyError:
            raise KeyError(f'{choice} is not a valid board choice. Choose from {list(Board.BOARDS_DATA.keys())}')
        lands_data, neighbor_data = board_data['lands'], board_data['neighbors']

        for id, land_data in lands_data.items():
            board.lands[id] = Land(**land_data)
        
        for id, neighbor_ids in neighbor_data.items():
            for neighbor_id in neighbor_ids:
                board.lands[id].add_neighbour(board.lands[neighbor_id])

        return board
