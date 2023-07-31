"""This class defines a square with a private instance attribute called size.

    Args:
        size (int): The size of the square.
    """
class Square:
    """This class defines a square with a private instance attribute called size.

    Args:
        size (int): The size of the square.
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """int: The area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
