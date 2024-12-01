# Exercise 54: Rectangle Class
# 1) Write a Rectangle class in Python, allowing to construct a rectangle with length and width attributes.
# 2) Create a Perimetre() method to calculate the perimeter of the rectangle and a Surface() method to calculate the surface of the rectangle.
# 3) Create the getters and setters.
# 4) Create a child class Parallelepipede inheriting from the Rectangle class and also having a height attribute and another Volume() method to calculate the volume of the Parallelepiped.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def Perimetre(self):
        return 2 * (self.__length + self.__width)

    def Surface(self):
        return self.__length * self.__width
    
    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height  # Make height private
    
    def Volume(self):
        return self.get_length() * self.get_width() * self.height  # Use getter methods for length and width
    
# Testing the code
p1 = Parallelepipede(2, 5, 2)
print(p1.Volume())  
