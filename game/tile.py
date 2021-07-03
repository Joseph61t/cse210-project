

class Tile():
    def __init__(self, x, y, block_type =0):
        self.x = x
        self.y = y
        self.block_type = block_type
    
    def set_block(self, block_type):
        self.block_type = block_type
    def get_block(self):
        return self.block_type