"""
Module for Rectangle class
"""
from models.base import Base
class Rectangle(Base):
    """
    Class for rectangle objects
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate of rectangle's position
            y (int): y-coordinate of rectangle's position
            id (int): unique identifier for rectangle object

        Returns:
            None
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width attribute

        Args:
            None

        Returns:
            int: width of rectangle object
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width attribute

        Args:
            value (int): new value for width attribute

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height attribute

        Args:
            None

        Returns:
            int: height of rectangle object
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height attribute

        Args:
            value (int): new value for height attribute

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x attribute

        Args:
            None

        Returns:
            int: x-coordinate of rectangle object's position
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x attribute

        Args:
            value (int): new value for x attribute

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y attribute

        Args:
            None

        Returns:
            int: y-coordinate of rectangle object's position
       """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        Setter for x attribute

        Args:
            value (int): new value for y attribute

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """
          returns the area value of the Rectangle instance.
        """
        return self.width * self.height
    def display(self): 
        for y in range(self.height):
            for x in range(self.width):
                if x == 0 or x == self.width - 1 or y == 0 or y == self.height - 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
    def __str__(self):
        return f"[Rectangle] ({id(self)}) {self.width}/{self.height}" 
    def update(self, *args,**kwargs):
        if args:
            for i, arg in enumerate(args):
             if i == 0:
                self.id = arg
             elif i == 1:
                self.width = arg    
             elif i == 2:
                self.height = arg   
             elif i == 3:
                self.x = arg     
             elif i == 4:
                self.y = arg  
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)  