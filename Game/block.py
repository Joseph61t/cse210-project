import arcade
from game.point import Point
from game import constants
from game.actor import Actor
import arcade

class Block(Actor):
    def __init__(self):
        super().__init__()
        
    def draw(self):
        arcade.draw_lrtb_rectangle_filled(100, 200, 400, 200, arcade.color.BLUE)
