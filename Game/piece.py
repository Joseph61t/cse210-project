import random

class Piece():
      def __init__(self):
            self.piece = {}
            self.rotation = 0
            self.velocity = (0,0)
            self.position = 186

            self.pieces = [
                  # 'I' 
                  # rot 1
                  [[0, 1, 0, 0, 
                  0, 1, 0, 0,
                  0, 1, 0, 0,
                  0, 1, 0, 0],
                  # rot 2 
                  [0, 0, 0, 0, 
                  0, 0, 0, 0,
                  1, 1, 1, 1,
                  0, 0, 0, 0], 
                  # rot 3
                  [0, 1, 0, 0, 
                  0, 1, 0, 0,
                  0, 1, 0, 0,
                  0, 1, 0, 0],
                  # rot 4
                  [0, 0, 0, 0, 
                  0, 0, 0, 0,
                  1, 1, 1, 1,
                  0, 0, 0, 0]], 
                  # 'L' 
                  # rot 1
                  [[0, 2, 0, 0, 
                  0, 2, 0, 0,
                  0, 2, 2, 0, 
                  0, 0, 0, 0], 
                  # rot 2 
                  [0, 0, 0, 0, 
                  2, 2, 2, 0,
                  2, 0, 0, 0, 
                  0, 0, 0, 0],
                  # rot 3
                  [0, 2, 2, 0, 
                  0, 0, 2, 0,
                  0, 0, 2, 0, 
                  0, 0, 0, 0],
                  # rot 4
                  [0, 0, 0, 0, 
                  0, 0, 2, 0,
                  2, 2, 2, 0, 
                  0, 0, 0, 0]],
                  # 'J'
                  # rot 1 
                  [[0, 0, 3, 0, 
                  0, 0, 3, 0,
                  0, 3, 3, 0, 
                  0, 0, 0, 0], 
                  # rot 2
                  [0, 0, 0, 0, 
                  3, 0, 0, 0,
                  3, 3, 3, 0, 
                  0, 0, 0, 0],
                  # rot 3
                  [0, 3, 3, 0, 
                  0, 3, 0, 0,
                  0, 3, 0, 0, 
                  0, 0, 0, 0],
                  # rot 4
                  [0, 0, 0, 0, 
                  3, 3, 3, 0,
                  0, 0, 3, 0, 
                  0, 0, 0, 0]],
                  # 'T'
                  # rot 1 
                  [[4, 4, 4, 0,
                  0, 4, 0, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0], 
                  # rot 2
                  [0, 4, 0, 0,
                  4, 4, 0, 0,
                  0, 4, 0, 0, 
                  0, 0, 0, 0],
                  # rot 3
                  [0, 4, 0, 0,
                  4, 4, 4, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0],
                  # rot 4
                  [0, 4, 0, 0,
                  0, 4, 4, 0,
                  0, 4, 0, 0, 
                  0, 0, 0, 0]],
                  # 'Z'
                  # rot 1 
                  [[5, 5, 0, 0,
                  0, 5, 5, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
                  # rot 2
                  [0, 5, 0, 0,
                  5, 5, 0, 0,
                  5, 0, 0, 0,
                  0, 0, 0, 0],
                  # rot 3
                  [5, 5, 0, 0,
                  0, 5, 5, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
                  # rot 4
                  [0, 5, 0, 0,
                  5, 5, 0, 0,
                  5, 0, 0, 0,
                  0, 0, 0, 0]],
                  # 'S'
                  # rot 1 
                  [[0, 6, 6, 0,
                  6, 6, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
                  # rot 2
                  [6, 0, 0, 0,
                  6, 6, 0, 0,
                  0, 6, 0, 0,
                  0, 0, 0, 0],
                  # rot 3
                  [0, 6, 6, 0,
                  6, 6, 0, 0,
                  0, 0, 0, 0,
                  0, 0, 0, 0],
                  # rot 4
                  [6, 0, 0, 0,
                  6, 6, 0, 0,
                  0, 6, 0, 0,
                  0, 0, 0, 0]],
                  # 'O' 
                  # rot 1
                  [[0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0], 
                  # rot2
                  [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0],
                  # rot3
                  [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0],
                  # rot4
                  [0, 7, 7, 0, 
                  0, 7, 7, 0,
                  0, 0, 0, 0, 
                  0, 0, 0, 0]]
                  ]
            self.set_piece()
            


      def set_piece(self):
            self.piece = random.choice(self.pieces)

      def rotate_right(self, coord_plane):
            can_rotate = self.can_rotate(coord_plane)
            if can_rotate == True:
                  if self.rotation < 3:
                        self.rotation += 1
                  else:
                        self.rotation = 0

      def rotate_left(self, coord_plane):
            can_rotate = self.can_rotate(coord_plane)
            if can_rotate == True:
                  if self.rotation > 0:
                        self.rotation -= 1
                  else:
                        self.rotation = 3

      def can_rotate(self, coord_plane):
            can_rotate = True
            for i in range(1,21):
                  if coord_plane[i*10].get_status() == 1 or coord_plane[(i*10) + 9].get_status() == 1:
                        can_rotate = False
            return can_rotate

      def get_piece(self):
            return self.piece[self.rotation]

      
                  

      
# piece = Piece()
# print(piece.piece)
# piece.set_rotation('@')
# print(piece.piece[piece.rotation])
# piece.set_rotation('#')
# print(piece.piece[piece.rotation])
