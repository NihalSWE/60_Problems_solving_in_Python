# Exercise 60: Geometry Class
# Write a Python class named Geometry with a default constructor without parameters.
# 1) Add a method named distance() to the geometry class that allows to calculate the distance between two points
# A = (a1, a2), B = (b1, b2) (with the convention: a point is identified by its coordinates M = (x M  , y M ) )
# 2) Add a method named middle() to the geometry class that allows to determine the middle of a bipoint (A , B).
# 3) Add a method named trianglePerimeter() to the geometry class that allows to calculate the perimeter of a triangle ABC.
# 4) Add a method named triangleIsoscel() that returns True if the triangle is isoscel and False otherwise.

import math

class Geometry:
    def __init__(self):
        pass
    # Method to calculate the distance between two points
    def distance(self, a1,a2,b1,b2):
        return math.sqrt((b1 - a1)**2 + (b2 - a2)**2)
    
    # Method to determine the middle of a bipoint (A , B)
    def middle(self, a1,a2,b1,b2):
        x= (a1 + b1)/2,
        y=(a2 + b2)/2,
        return (x,y)
    
    # 4. Method to calculate the perimeter of a triangle
    def trianglePerimeter(self, A, B, C):
        # Unpack points A, B, C
        a1, a2 = A
        b1, b2 = B
        c1, c2 = C
        
        # Calculate distances (sides of the triangle)
        AB = self.distance(a1, a2, b1, b2)
        BC = self.distance(b1, b2, c1, c2)
        CA = self.distance(c1, c2, a1, a2)
        
        # Perimeter is the sum of the sides
        return AB + BC + CA


    # 5. Method to check if the triangle is isosceles
    def triangleIsoscel(self, A, B, C):
        # Unpack points A, B, C
        a1, a2 = A
        b1, b2 = B
        c1, c2 = C
        
        # Calculate distances (sides of the triangle)
        AB = self.distance(a1, a2, b1, b2)
        BC = self.distance(b1, b2, c1, c2)
        CA = self.distance(c1, c2, a1, a2)
        
        # Check if two sides are equal (isosceles condition)
        return AB == BC or BC == CA or AB == CA



t1=Geometry()
print(f"the distance of 2 ponts {t1.distance(2,3,4,5):.2f}")
print(f"the middle of 2 ponts {t1.middle(2,3,4,5)}")
# Example 3: Calculate the perimeter of triangle ABC with points A(1, 1), B(4, 1), and C(4, 5)
print("Perimeter:", t1.trianglePerimeter((1, 1), (4, 1), (4, 5)))

# Example 4: Check if triangle ABC is isosceles
print("Isosceles:", t1.triangleIsoscel((1, 1), (4, 1), (4, 5)))
