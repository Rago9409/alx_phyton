"""This is module for Base class."""
class Base:
 """This code program  defines a class Base that is 
 the base class aimed to manage id attribute."""
 __nb_objects = 0
 """This code program defines a class constructor."""
def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
