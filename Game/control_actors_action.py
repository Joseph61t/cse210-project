from game.board import Board
from game.piece import Piece
from game.block import Block
from game import constants
from game.action import Action

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        board = cast["board"][0] # there's only one in the cast
        direction = self._input_service.get_direction()
        if direction[0] == 1:
            board.update_left()
        if direction[0] == -1:
            board.update_right()
        if direction[1] == -3:
            board.move_down_faster()
        if self._input_service.should_rotate_left():
            board.piece.rotate_left()
        elif self._input_service.should_rotate_right():
            board.piece.rotate_right()