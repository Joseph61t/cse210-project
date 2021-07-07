import arcade

class Tile(arcade.Sprite):
    def __init__(self, x=0, y=0, block_type =0, color = "game/blocks/red-block.png"):
        super().__init__(color)
        self._set_scale(.07)
        self.block_type = block_type
        self._set_position((x,y))
        self.status = 0 

    def set_block(self, block_type):
        self.block_type = block_type
        
    def get_block(self):
        return self.block_type
    
    def set_status(self, alive):
        self.status = alive
    
    def set_color(self):
        self.color = "game/background.png"