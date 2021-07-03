import arcade

class Tile(arcade.Sprite):
    def __init__(self, x=0, y=0, block_type =0):
        super().__init__("game/background.png")
        self._set_scale(.07)
        self.block_type = block_type
        self._set_position((x,y))

    def set_block(self, block_type):
        self.block_type = block_type
        
    def get_block(self):
        return self.block_type