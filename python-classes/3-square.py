"""
    This program code  represents a square.

    Attributes:
        __size (int): The size of the square.

    """
class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.

    """
    def __init__(self, size=0):
        """
    This function represents a square.

    Attributes:
        __size (int): The size of the square.

    """
        self.size = size

    @property
    def size(self):
        """
    This function  represents a square setting property.

    Attributes:
        __size (int): The size of the square.

    """
        return self.__size

    @size.setter
    def size(self, value):
        """
    This function represents a square with  setting property.

    Attributes:
        __size (int): The size of the square.

    """
        if not isinstance(value, int):
            """
    This Checks  a square value is integer.

    Attributes:
        __size (int): The size of the square.

    """
            raise TypeError("size must be an integer")
        elif value < 0:
            """
    This checks  a square value not integer.

    Attributes:
        __size (int): The size of the square.

    """
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
    This function returns the current square area.

    Attributes:
        __size (int): The size of the square.

    """
        return self.__size ** 2
