from math import trunc
from game.director import Director
import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService
from game.block import Block
from game.piece import Piece

from game.board import Board
import time


import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    start = (250, 550)

    
    # block = Block()
    # piece = Piece()
    # block._set_scale(.07)
    # block._set_position(start)
    # block._set_change_y(-1)
    board = Board()
    cast ["board"] = [board]
    # cast ["pieces"] = [piece]
        
    
    # test = Board()
    # piece = Piece()
    # index = 0
    # test.load_piece(piece)
    # grid = test.get_board()
    # index = 0
    
    # while index < 200:
    #     print(f' {grid[index].get_block()} {grid[index + 1].get_block()} {grid[index + 2].get_block()} {grid[index + 3].get_block()} {grid[index + 4].get_block()} {grid[index + 5].get_block()} {grid[index + 6].get_block()} {grid[index + 7].get_block()} {grid[index + 8].get_block()} {grid[index + 9].get_block()}')
    #     index += 10
    
    


    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script, input_service)
    director.setup()
    arcade.run()


if __name__ == "__main__":
    main()