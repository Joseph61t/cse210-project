from game.tile import Tile
from game.block import Block
from game.piece import Piece
import arcade

class Board():# create a large grid as the board
    def __init__(self):
        self.coord_plane = self.create_board()
        self.frames = 0
        self.load_piece()
        self.description = "board"
        self.piece = Piece()



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
            board[i].set_status(0)
            self.set_color(board[i])

        

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

        #double frame count, and divide by odd and even to allow for movement, or rotation.
        if self.frames % 80 == 79:
            self.piece.position -= 10

        if self.frames % 80 == 79:

            for i in range(0,210):
                if self.coord_plane[i].status == 1:
                    # self.transpose_piece_to_board()
                    self.coord_plane[i - 10].set_block(1)
                    self.coord_plane[i - 10].set_status(1)
                    self.coord_plane[i].set_block(0)
                    self.coord_plane[i].set_status(0)
            self.frames += 1 
                    
        else:
            self.frames += 1
        
        
        lines_to_delete = []
        for i in range(1,21):
            line_counter = 0
            for j in range(0,10):
                if self.coord_plane[(i*10) + j].get_block() != 0 and self.coord_plane[(i*10) + j].get_status() == 0:
                    line_counter += 1
            if line_counter == 10:
                lines_to_delete.append(i)
        if len(lines_to_delete) > 0:
            for line in lines_to_delete:
                for j in range(0,10):
                    self.coord_plane[(line * 10) + j].set_block(0)
                    self.coord_plane[(line * 10) + j].set_status(0)



    def move_down_faster(self):
        for i in range(0,210):
            if self.coord_plane[i].get_status() == 1:
                self.coord_plane[i-10].set_block(1)
                self.coord_plane[i-10].set_status(1)
                self.coord_plane[i].set_block(0)
                self.coord_plane[i].set_status(0)



    def update_left(self):
        if self.piece.position % 10 != 2:
            self.piece.position -= 1
            for i in range(0,210):
                if self.coord_plane[i].get_status() == 1 and self.coord_plane[i].get_left() == 1:
                    self.coord_plane[i-1].set_block(self.coord_plane[i].get_block())
                    self.coord_plane[i-1].set_status(1)
                    self.coord_plane[i].set_block(0)
                    self.coord_plane[i].set_status(0)

    def update_right(self):
        if self.piece.position % 10 != 9:
            list_of_alive = []
            index = 200
            self.piece.position += 1
            while index > 0:
                if self.coord_plane[index].get_status() == 1 and self.coord_plane[index].get_right() == 1:
                    list_of_alive.append(index+1)
                    self.coord_plane[index].set_block(0)
                    self.coord_plane[index].set_status(0)
                index -= 1
            for item in list_of_alive:
                self.coord_plane[item].set_block(1)
                self.coord_plane[item].set_status(1)
    
    def load_piece(self):
        self.piece = Piece()
        
        x = 0
        y = 0
        board_index = self.piece.position
        piece_index = 0
        piece_grid = self.piece.get_piece() # this is to get the proper rotation

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
  
    def transpose_piece_to_board(self):
        for i in range(0,self.piece.position): # the base of the board is regular tiles
            if self.coord_plane[i].status == 1:    
                self.coord_plane[i].set_block(0)
                self.coord_plane[i].set_status(0)
        x = 0
        y = 0
        board_index = self.piece.position
        piece_index = 0
        piece_grid = self.piece.get_piece() # this is to get the proper rotation
        while y < 4:
            x = 0
            while x < 4:
                if piece_grid[piece_index] != 0: # if in the piece grid the certain index is empty or not
                    print(board_index)
                    self.coord_plane[board_index].set_block(piece_grid[piece_index]) # sets the tile value to the value from the piece (1-6)
                    self.coord_plane[board_index].set_status(1) 
                board_index -= 1
                piece_index += 1
                x += 1
            board_index -= 6 # to skip to the next line
            y += 1
  
  
    def set_color(self, tile):
        tile.texture = arcade.load_texture(f"game/blocks/background.png")
        
        
          
   
