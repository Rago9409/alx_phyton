"""
Module for Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class for square objects
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object

        Args:
            size (int): size of square
            x (int): x-coordinate of square's position
            y (int): y-coordinate of square's position
            id (int): unique identifier for square object

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns string representation of Square object

        Args:
            None

        Returns:
            str: string representation of Square object
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width)
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value