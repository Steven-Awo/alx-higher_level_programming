#!/usr/bin/python3
"""Defining new a Rectangle class."""


class Rectangle:
    """Representation the new rectangle.

    Attributes:
        number_of_instances (int): The number of instances in rectangle.
        print_symbol (any): The symbol to be used for string representations.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializating a new Rectangle.

        Args:
            height (int): The height of the new rectangle.
            width (int): The width of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting/setting the width of the new rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting/setting the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returning the calculated area of the Rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returning the calculated perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returning the greater area between rectangles.

        Args:
            rect_1 (Rectangle): The 1st rectangle.
            rect_2 (Rectangle): The 2nd rectangle.
        Raises:
            TypeError: If either rect_1 or rect_2 is not a rectangle.
        """
        if isinstance(rect_1, Rectangle) is not True:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is not True:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def __str__(self):
        """Returning the printable, representations of the Rectangle.

        Representing or creating the rectangle with the # char.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        rectc = []
        for x in range(self.__height):
            [rectc.append(str(self.print_symbol)) for y in range(self.__width)]
            if x != self.__height - 1:
                rectc.append("\n")
        return ("".join(rectc))

    def __repr__(self):
        """Returning the str representations of the rectangle."""
        rectc = "Rectangle(" + str(self.__width)
        rectc += ", " + str(self.__height) + ")"
        return (rectc)

    def __del__(self):
        """Printing a message for everytime a deletion of a rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
