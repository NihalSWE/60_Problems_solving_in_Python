# Exercise 52   : Rectangle class
# Write  in Python  a program using a rectangle class whose constructor takes two parameters, width and  height, and which offers the following functions:
# 1) calculation of the perimeter
# 2) surface calculation
# 3) display as well as trivial accessors and mutators (reading and modifying width and height).

class Rectangle:
    # Constructor to initialize width and height
    def __init__(self, width, height):
        self.__width = width  # Private variable for width
        self.__height = height  # Private variable for height

    # Method to calculate the perimeter of the rectangle
    def perimeter(self):
        return 2 * (self.__width + self.__height)
    
    # Method to calculate the surface (area) of the rectangle
    def surface(self):
        return self.__width * self.__height

    # Method to display the width and height
    def display(self):
        print(f"Rectangle: Width = {self.__width}, Height = {self.__height}")

    # Accessor for width
    def get_width(self):
        return self.__width
    
    # Accessor for height
    def get_height(self):
        return self.__height
    
    # Mutator for width
    def set_width(self, width):
        self.__width = width
    
    # Mutator for height
    def set_height(self, height):
        self.__height = height

# Example usage:
r1 = Rectangle(5, 10)

# Display the dimensions of the rectangle
r1.display()

# Calculate and print the perimeter and surface (area)
print("Perimeter:", r1.perimeter())
print("Surface:", r1.surface())

# Using mutators to change the width and height
r1.set_width(7)
r1.set_height(12)

# Display the updated dimensions
r1.display()

# Calculate and print the updated perimeter and surface (area)
print("Updated Perimeter:", r1.perimeter())
print("Updated Surface:", r1.surface())
