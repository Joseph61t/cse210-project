import arcade

class Tile(arcade.Sprite):
    def __init__(self, x=0, y=0, block_type =0, color="game/blocks/blue-block.png"):

        super().__init__(color)
        self._set_scale(.05)
        self.block_type = block_type
        self._set_position((x,y))
        self.status = 0 
        self.canLeft = 1
        self.canRight = 1

    def set_block(self, block_type):
        self.block_type = block_type

    def get_block(self):
        return self.block_type
    
    def set_status(self, alive):
        self.status = alive

    def get_status(self):
        return self.status

    def set_left(self, left):
        self.canLeft = left

    def set_right(self, right):
        self.canRight = right

    def get_left(self):
        return self.canLeft

    def get_right(self):
        return self.canRight

    def set_color(self, color="background"):
        self.texture = arcade.load_texture(f"game/blocks/{color}-block.png")
    

