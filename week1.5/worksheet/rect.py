# Worksheet 1.5: Rectangle Class
class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        Raises TypeError if width or height is not an integer.
        Raises ValueError if width or height <= 0.
        """
        if not isinstance(width, int):
            raise TypeError
        if not isinstance(height, int):
            raise TypeError
        if width <= 0:
            raise ValueError
        if height <= 0:
            raise ValueError
        self.width = width
        self.height = height

    def is_square(self):
        """Return True if this rectangle is a square, False otherwise."""
        return self.width == self.height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)