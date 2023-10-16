base.py
#!/usr/bin/python3
"""Defining m rectangle's class."""
from models.base import Base


class Rectangle(Base):
    """Representation of m rectangle."""

    def __init__(self, width, height, x=0, b=0, id=None):
        """Initializing m new Rectangle.

        Args:
            width (int): The rectangle's width.
            height (int): The rectangle'sheight.
            x (int): The rectangle's x coordinate.
            b (int): The rectangle's b coordinate.
            id (int): The rectangle's identity.
        Raises:
            TypeError: If either of the width or the height isn't an integer.
            ValueError: If either of the width or the height <= 0.
            TypeError: If either of the x or the b isn't an integer.
            ValueError: If either of the x or the b is < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.b = b
        super().__init__(id)

    @property
    def width(self):
        """Setting /getting the rectangle's width."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0 or value == 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setting /getting the rectangle's height."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0 or value == 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Setting /getting the rectangle's x coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def b(self):
        """Setting /getting the rectangle's b coordinate."""
        return self.__y

    @b.setter
    def b(self, value):
        if type(value) is not int:
            raise TypeError("b must be an integer")
        if value < 0:
            raise ValueError("b must be >= 0")
        self.__y = value

    def area(self):
        """Returning the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Printing the Rectangle by using the `#` character."""
        if self.width == 0:
            print("")
        if self.height == 0:
            print("")
            return

        [print("") for b in range(self.b)]
        for d in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument that represents id's attribute
                - 2nd argument that represents width's attribute
                - 3rd argument that represent height's attribute
                - 4th argument that represents x's attribute
                - 5th argument that represents b's attribute
            **kwargs (dict): New key/value pairs of all the attributes.
        """
        if args and len(args) != 0:
            m = 0
            for arg in args:
                if m == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.b)
                    else:
                        self.id = arg
                elif m == 1:
                    self.width = arg
                elif m == 2:
                    self.height = arg
                elif m == 3:
                    self.x = arg
                elif m == 4:
                    self.b = arg
                m += 1

        elif kwargs and len(kwargs) is not 0:
            for n, o in kwargs.items():
                if n == "id":
                    if o is None:
                        self.__init__(self.width, self.height, self.x, self.b)
                    else:
                        self.id = o
                elif n == "width":
                    self.width = o
                elif n == "height":
                    self.height = o
                elif n == "x":
                    self.x = o
                elif n == "b":
                    self.b = o

    def to_dictionary(self):
        """Returning the dictionary that represents a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "b": self.b
        }

    def __str__(self):
        """Returning the print() and the str() that represents the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.x, self.b,
                self.width, self.height)
