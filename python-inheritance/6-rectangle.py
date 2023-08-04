"""This is a class BaseGeometry"""
    """This Function raises an Exception with the message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
    """This Function validates value"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")f
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
"""This is a class Rectangle inherits class BaseGeometry"""
class Rectangle(BaseGeometry):
    """This Function instantiates width and height """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    