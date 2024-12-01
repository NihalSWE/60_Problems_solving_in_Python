# Exercise 53   : Inheritance 
# Write a program  in Python  that defines a class called Shape with a constructor that sets the width(x) and height(y) values. Define the area() method in both the Triangle and Rectangle subclasses, which calculate the area. In the main method, main, define two variables, a triangle and a rectangle, and then call the area() function in both of these variables.
# Note that:
# the area of ​​the triangle is = width * height / 2 
# the area of ​​the rectangle is = width * height.

# Base class Shape
class Shape:
    def __init__(self, x, y):
        self.x = x  # width
        self.y = y  # height

# Subclass Triangle inheriting from Shape
class Triangle(Shape):
    def area(self):
        # Formula for the area of a triangle: width * height / 2
        return (self.x * self.y) / 2

# Subclass Rectangle inheriting from Shape
class Rectangle(Shape):
    def area(self):
        # Formula for the area of a rectangle: width * height
        return self.x * self.y

# Main function to test the classes
def main():
    # Create an instance of Triangle
    triangle = Triangle(4, 8)
    print(f"X={triangle.x} Y={triangle.y}")
    print(f"Area of Triangle: {triangle.area()}")  # Should print 16.0

    # Create an instance of Rectangle
    rectangle = Rectangle(5, 6)
    print(f"X={rectangle.x} Y={rectangle.y}")
    print(f"Area of Rectangle: {rectangle.area()}")  # Should print 30

# Call the main function
if __name__ == "__main__":
    main()
