"""This is a class Square"""
class Square:
    """This Function instantiates size """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
    """This should return str """
    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
