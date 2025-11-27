class Rectangle:
    def __init__(self, length=0, width=0):
        self.__length = length   # private attribute
        self.__width = width     # private attribute

    # method to compute area
    def area(self):
        return self.__length * self.__width

    # overload < operator
    def __lt__(self, other):
        return self.area() < other.area()


# Example usage
r1 = Rectangle(4, 5)
r2 = Rectangle(3, 10)

if r1 < r2:
    print("Rectangle r1 is smaller than r2")
else:
    print("Rectangle r1 is NOT smaller than r2")
