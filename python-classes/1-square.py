"""This module defines a square with a private instance attribute called size.

    Args:
        size (int): The size of the square.
    """
class Square:
    """This Class defines a square with a private instance attribute called size.
    
    Args:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        The constructor for Square class.

        Parameters:
            size (int): The size of the square.

        """
        self.__size = size

        if type(size) != int:
            """
        The size must integer.
        """
            raise TypeError("size must be an integer")
        elif size < 0:
            """
         The size of the square less than 0.

        """
            raise ValueError("size must be >= 0")
