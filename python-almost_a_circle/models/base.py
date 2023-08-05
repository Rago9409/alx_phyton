"""This code program  defines a class Base.
    """
class Base:
 __nb_objects = 0
 """This code program  class constructor.
    """
def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
