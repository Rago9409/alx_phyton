"""This is module for Base class."""
class Base:
 """This code program  defines a class Base that is 
 the base class aimed to manage id attribute."""
 __nb_objects = 0
def __init__(self, id=None):
        """
        Initializes a Base object

        Args:
            id (int): unique identifier for Base object

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
