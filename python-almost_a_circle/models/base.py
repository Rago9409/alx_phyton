"""This is module for Base class."""
class Base:
    """
    Class for base objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object

        Args:
            id (int): unique identifier for base object

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
