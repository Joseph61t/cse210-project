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
        block = cast["blocks"][0]
        position= block._get_position()
        if position[1] < 30:
            block._set_change_x(0)
            block._set_change_y(0)
        if position[0] <= 21:
            block._set_change_x(0)
        elif position[0] >= 479:
            block._set_change_x(0)
            
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

        #set up colliding with walls
        # if ball.get_position().get_x() - 1 == MAX_X:
        #     point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
        #     ball.set_velocity(point)
        # if ball.get_position().get_x() + 1 == 0:
        #     point = Point((ball.get_velocity().get_x() * -1), ball.get_velocity().get_y())
        #     ball.set_velocity(point)
        # if ball.get_position().get_y() - 1 == 0:
        #     point = Point(ball.get_velocity().get_x(), (ball.get_velocity().get_y() * -1))
        #     ball.set_velocity(point)
            
             

        # Setting up the paddle points
        # firstX = paddle.get_position().get_x()
        # lastX = firstX + 12
        # y = paddle.get_position().get_y()
        # fullPaddle = []
        # for x in range(firstX, lastX):
        #     point = (x,y)
        #     fullPaddle.append(point)
        
        # The if statments that govern when the ball hits the paddle
        # for x in fullPaddle:
        #     pos_x = x[0]
        #     pos_y = x[1]
        #     if ball.get_position().get_y() + 1 == pos_y and ball.get_position().get_x() == pos_x:
        #             point = Point(ball.get_velocity().get_x(), (ball.get_velocity().get_y() * -1))
        #             ball.set_velocity(point)

        # the if statements the cover when a ball hits a brick
        # covers if the ball hits a brick from below
        
        # void = Point(1000,1000)
        
        
        