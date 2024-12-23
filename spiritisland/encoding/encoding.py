from board import Land, Board

class Encoding():
    def __init__(self):
        pass
    

    @staticmethod
    def encode_land(land : Land):
        temp = [land.id, land.presences, land.dahans, land.blight, land.explorers, land.towns, land.cities, land.defense]
        return  temp
    
    @staticmethod
    def encode_board(board : Board):
        temp = []
        for land in board:
            for properties in land:
                temp.append(properties)
         
