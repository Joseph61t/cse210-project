from game import constants
from game.action import Action
from game.point import Point
import arcade

class MoveActorsAction(Action, arcade.Sprite):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for block in group:
                block.update()
                



    def _move_actor(self, actor):
        """Moves the given actor to its next position according to its 
        velocity. Will wrap the position from one side of the screen to the 
        other when it reaches the edge in either direction.
        
        Args:
            actor (Actor): The actor to move.
        """

        position = actor.get_position()
        velocity = actor.get_velocity()
        x_pos = position.get_x()
        y_pos = position.get_y()
        x_vel = velocity.get_x()
        y_vel = velocity.get_y()

        x_new = (x_pos + x_vel )
        y_new = (y_pos + y_vel ) 
        position = Point(x_new, y_new)
        actor.set_position(position)

    