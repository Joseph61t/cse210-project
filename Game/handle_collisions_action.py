from game.board import Board
from game.constants import MAX_X
from game.constants import MAX_Y
from game import point
import random
from game import constants
from game.action import Action
from game.point import Point
import sys
class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        board = cast["board"][0]
        # position= block._get_position()
        # if position[1] < 20:
        #     piece._set_change_x(0)
        #     piece._set_change_y(0)
        # if position[0] <= 20:
        #     piece._set_change_x(0)
        # elif position[0] >= 480:
        #     piece._set_change_x(0)
            
        # for block in blocks:
        #     if ball.get_position().get_y() - 1 == brick.get_position().get_y() and ball.get_position().get_x() == brick.get_position().get_x():
        #         point = Point(ball.get_velocity().get_x(), (ball.get_velocity().get_y() * -1))
        #         ball.set_velocity(point)
                
        #         brick.set_position(void)
                
        #     # covers if the ball hits a brick from above
        #     if ball.get_position().get_y() + 1 == brick.get_position().get_y() and ball.get_position().get_x() == brick.get_position().get_x():
        #         point = Point(ball.get_velocity().get_x(), (ball.get_velocity().get_y() * -1))
        #         ball.set_velocity(point)
                
        #         brick.set_position(void)
                
        #     # covers if the ball hits a brick from the left
        #     if ball.get_position().get_x() - 1 == brick.get_position().get_x() and ball.get_position().get_y() == brick.get_position().get_y():
        #         point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
        #         ball.set_velocity(point) 
                
        #         brick.set_position(void)
                
        #     # covers if the ball hits a brick from the right
        #     if ball.get_position().get_x() + 1 == brick.get_position().get_x() and ball.get_position().get_y() == brick.get_position().get_y():
        #         point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
        #         ball.set_velocity(point)
                
        #         brick.set_position(void)

        
            
        
        
        
        