import random
from game.casting.actor import Actor
from game.shared.point import Point


class Gem(Actor):
    """
    An item of cultural or historical interest. 

    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """

    def __init__(self):
        super().__init__()
        self._message = ""
        self._gem_value = 0

    def set_gem_value(self):
        self._gem_value = random.randint(5, 20)

    def get_gem_value(self):
        return self._gem_value

    def get_message(self):
        """Gets the artifact's message.

        Returns:
            string: The message.
        """
        return self._message

    def set_message(self, message):
        """Updates the message to the given one.

        Args:
            message (string): The given message.
        """
        self._message = message

    def move_next(self, max_x, max_y):
        """copied from parent actor.py

        Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        # self._position = Point(x, y)
        if y > int(15 * 34):
            self._position = Point(x,
                                   y + 1)
        else:
            self._position = Point(x,
                                   y + random.randint(1, 5))
        if y > int(15 * 36):
            self._position = Point(x,
                                   y + random.randint(1, 5))
