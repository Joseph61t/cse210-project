from game.tile import Tile
from game.block import Block
from game.piece import Piece

class Board():# create a large grid as the board
    def __init__(self):
        self.coord_plane = self.create_board()
        self.frames = 0
        self.load_piece()
        

    def create_board(self): # create a board with 50px border
        board = []
        for i in range(0,21):
            for j in range(0,10):
                 #size of block is 40px wide and starting spot is at 70 (50px border, 20px radius)
                position = ((100+(j*35)),(100+(i*35)))
                tile = Tile()
                tile._set_position(position)
                board.append(tile)

        for i in range(0,10): # the base of the board is regular tiles
            board[i].set_block(1)
            board[i].status = 0
            board[i].texture = "game/background.png"
        
        return board

    def get_board(self):
        return self.coord_plane


    def draw(self):
        for tile in self.coord_plane:
            if tile.get_block() != 0:
                tile.set_block(1)
                tile.draw()

    

    def update(self):
        # makes piece move down
        if self.frames % 10 == 1:
            for i in range(0,210):
                if self.coord_plane[i].status == 1:
                    self.coord_plane[i-10].set_block(1)
                    self.coord_plane[i-10].set_status(1)
                    self.coord_plane[i].set_block(0)
                    self.coord_plane[i].set_status(0)
            self.frames += 1 
                    
        else:
            self.frames += 1


    def load_piece(self):
        piece = Piece()
        
        x = 0
        y = 0
        board_index = piece.position
        piece_index = 0
        piece_grid = piece.get_piece() # this is to get the proper rotation
        while y < 4:
            x = 0
            while x < 4:
                if piece_grid[piece_index] != 0: # if in the piece grid the certain index is empty or not
                    self.coord_plane[board_index].set_block(piece_grid[piece_index]) # sets the tile value to the value from the piece (1-6)
                    self.coord_plane[board_index].set_status(1) 
                board_index -= 1
                piece_index += 1
                x += 1
            board_index -= 6 # to skip to the next line
            y += 1
        # board_index = 166 # this is a trivial number to put the piece at the top of the board
        # piece_index = 0
        # piece_grid = piece.get_piece() # this is to get the proper rotation
        # while y < 4:
        #     x = 0
        #     while x < 4:
        #         if piece_grid[piece_index] != 0: # if in the piece grid the certain index is empty or not
        #             self.coord_plane[board_index].set_block(piece_grid[piece_index]) # sets the tile value to the value from the piece (1-6)
        #         board_index -= 1
        #         piece_index += 1
        #         x += 1
        #     board_index -= 6 # to skip to the next line
        #     y += 1
        
           




