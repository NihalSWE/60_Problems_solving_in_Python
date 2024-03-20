# Exercise 46  : Rectangle class 
# Write in Python a “Rectangle” class having two variables “a” and “b” and a member function “surface()” which will return the surface of the rectangle.

class Rectangle:
    def __init__(self,a=0,b=0):
        self.A=a
        self.B=b
    
    def surface(self):
        return self.A*self.B
        
R1=Rectangle(5,10)
R2=Rectangle()
print("Surface of R1 =",R1.surface())
print("Surface of R2 =",R2.surface())