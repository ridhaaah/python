class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    # Method to find area
    def area(self):
        return self.length * self.breadth

    # Method to find perimeter
    def perimeter(self):
        return 2 * (self.length + self.breadth)

    # Compare rectangles by area
    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()


# Example usage:
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 7)

print("Area of r1:", r1.area())
print("Area of r2:", r2.area())
print("Perimeter of r1:", r1.perimeter())
print("Perimeter of r2:", r2.perimeter())

# Comparison by area
if r1 > r2:
    print("r1 is larger than r2 in area")
elif r1 < r2:
    print("r1 is smaller than r2 in area")
else:
    print("Both rectangles have equal area")
