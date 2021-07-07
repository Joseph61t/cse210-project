import sys
from game.point import Point

import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []
    
    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)

    def get_direction(self, block):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = -1
        position = block._get_position()

        if position[1] > 20:
            if arcade.key.LEFT in self._keys:
                x = 1
            elif arcade.key.RIGHT in self._keys:
                x = -1
            if arcade.key.DOWN in self._keys: # speeds up the block
                y = -4
            elif arcade.key.UP in self._keys: # moves the block to the bottom of the screen
                position[1] = 20
                block._set_position(position)
            

            velocity = (x, y)
            return velocity
        
        
    def rotation(self, key,  piece):
        if arcade.key.D in self._keys:
            piece._set_rotation(key)
        elif arcade.key.A in self._keys:
            piece._set_rotation(key)

            

