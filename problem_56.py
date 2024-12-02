# Exercise 56: Circle Class
# 1) Define a Circle class to create a circle C(O,r) with center O(a,b) and radius r using the constructor:
# 2) Define a Surface() method of the class to calculate the surface area of ​​the circle
# 3) Define a Perimetre() method of the class to calculate the perimeter of the circle
# 4) Define a testAppartenance() method of the class to test whether or not a point A(x,y) belongs to the circle C(O,r).

import math

class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def Surface(self):
        return math.pi * (self.r ** 2)
    
    def Perimetre(self):
        return 2 * math.pi * self.r
    
    def testAppartenance(self,x,y):
        distance_squared = (x - self.a )**2 + (y - self.b)**2 

        if distance_squared == self.r**2 :
            return True
        else:
            return False

c1=Circle(3,4,5)
print(f"Surface area: {c1.Surface():.2f}")  # Should print the area of the circle
print(f"Perimeter: {c1.Perimetre():.2f}")  # Should print the perimeter of the circle

# Check if a point (3, 4) belongs to the circle
print("Point (3, 4) belongs to the circle:", c1.testAppartenance(3, 4))  # Should return True or False