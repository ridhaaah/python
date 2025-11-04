square_area = lambda side: side * side
rectangle_area = lambda length, width: length * width
triangle_area = lambda base, height: 0.5 * base * height
side = float(input("Enter side of square:"))
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
print("Area of square:", square_area(side))
print("Area of rectangle:", rectangle_area(length, width))
print("Area of triangle:", triangle_area(base, height))

