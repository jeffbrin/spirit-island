
class BlightPool():
    def __init__(self, blight_count: int = 5):
        self.blight_count = blight_count
        
    def add(self) -> int:
        self.blight_count += 1
        return self.blight_count
        
    def remove(self) -> int:
        self.blight_count -= 1
        return self.blight_count
        
