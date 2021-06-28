import random

class Piece:
    def __init__(self) -> None:
        self.piece = []
        self.rotation = 0

    def set_piece(self):
        pieces = {
            'I': [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], 
            'L': [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
            'J': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            'T': [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'Z': [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'S': [0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            'O': [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            }
        pieceList = list(pieces.items())
        self.piece = random.choice(pieceList)

    def set_rotation(self, key):
        if key == "#":
            if self.rotation < 4:
               self.rotation += 1
            else:
                self.rotation = 0
        elif key == "#":
            if self.rotation > 0:
                self.rotation -= 1
            else:
                self.rotation = 4
        else:
            pass
