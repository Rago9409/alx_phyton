"""This is a class Rectangle"""
class Rectangle:
    """This Function instantiates width and height """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """This method returns  width and height """
    def area(self):
        return self.__width * self.__height
    """This Function should return str """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
