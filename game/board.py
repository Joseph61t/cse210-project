from tile import Tile

class Board():# create a large grid as the board
    def __init__(self):
        self.coord_plane = self.create_board()

    def create_board(self): # create a board with 50px border
        board = []
        for i in range(0,10):
            for j in range(0,20):
                 #size of block is 40px wide and starting spot is at 70 (50px border, 20px radius)
                board.append(Tile(70+(i*40),70+(j*40)))
        return board

# test = Board()
# print(test.coord_plane[199].x)
# print(test.coord_plane[199].y)