from game.point import Point
from game import constants

import arcade

class Piece(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("""NEED TO CHANGE TO DRAW""")

        # something to add to draw
        self.center_x = x
        self.center_y = y