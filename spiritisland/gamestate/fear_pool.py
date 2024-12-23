from gamestate import GameState

class FearPool(GameState):
    def __init__(self, fear_count: int = 5):
        self.fear_count = fear_count
        self.max_fear = fear_count

    def reset_pool(self):
        self.fear_count = self.max_fear
        
    def generate_fear(self):
        self.fear_count -= 1
