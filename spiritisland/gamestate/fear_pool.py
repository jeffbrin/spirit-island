from gamestate import GameState

class FearPool(GameState):
    def __init__(self, fearpool: int = 5):
        self.fearpool = fearpool

    def reset_pool(self):
        self.fearpool + 5
        
    def remove_from_pool(self):
        self.fearpool -1
        if FearPool.fearpool == 0:
            FearPool.reset_pool()

            
    
    
