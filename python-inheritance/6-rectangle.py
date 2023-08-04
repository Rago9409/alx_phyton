"""This is a class Rectangle"""
class Rectangle:
    """This Function instantiates width and height """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height