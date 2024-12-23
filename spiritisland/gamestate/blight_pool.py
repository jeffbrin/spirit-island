from .gamestate import GameState

class BlightPool(GameState):
    def __init__(self, blightpool: int = 5):
        self.blightpool = blightpool
        # TODO NEED TO ADD LOSING CONDITION IF BLIGHTPOOL = 0
        
    def add_to_pool(self):
        return self.blightpool + 1
        
    def remove_to_pool(self):
        return self.blightpool - 1
        
