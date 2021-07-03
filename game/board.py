from game.tile import Tile
from game.block import Block

class Board():# create a large grid as the board
    def __init__(self):
        self.coord_plane = self.create_board()

    def create_board(self): # create a board with 50px border
        board = []
        for i in range(0,10):
            for j in range(0,21):
                 #size of block is 40px wide and starting spot is at 70 (50px border, 20px radius)
                board.append(Tile(100+(i*35),100+(j*35)))
        return board
    def draw(self):
        for tile in self.coord_plane:
            if tile.block_type != 0:
                block = Block()
                block._set_scale(.07)
                position =  (tile.x, tile.y)
                block._set_position(position)
                block.draw()
    def update(self):
        pass

# test = Board()
# print(test.coord_plane[199].x)
# print(test.coord_plane[199].y)
