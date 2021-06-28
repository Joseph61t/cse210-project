

class Tile():
    def __init__(self, x, y, block_type):
        self.x = x
        self.y = y
        self.block_type = block_type
    
    def set_color(self, block_type):
        self.block_type = block_type