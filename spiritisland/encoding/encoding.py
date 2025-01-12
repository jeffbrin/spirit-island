from board import Land, Board
import pandas as pd

class Encoding():
    def __init__(self):
        pass
    

    @staticmethod
    def encode_land(land : Land):
        temp = [land.presences, land.dahans, land.blight, land.explorers, land.towns, land.cities, land.defense]
        return  temp
    
    @staticmethod
    def encode_board(board : Board):
        temp = []
        for land in board:
            for properties in land:
                temp.append(properties)

        df = pd.DataFrame()
        return temp
    
class Decoding():
    def __init__(self):
        pass

    @staticmethod
    def update_board(code : Encoding):
        
        return 

    
    

         
