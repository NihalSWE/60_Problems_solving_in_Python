# Exercise 49  : point class
# Create  a point class in Python   to manipulate a point on a plane. We will provide:
# 1) a point is defined by its x and y coordinates (private members)
# 2) the manufacturers 
# 3) a member function moves performing a translation defined by its two arguments dx and dy (double)
# 4) a member function displays simply displaying the Cartesian coordinates of the point.+
# 5) a member function enter simply entering the Cartesian coordinates of the point.
# 6) a distance member function calculating the distance between two points.
# 7) a midpoint member function giving the midpoint of a segment.
# 8) a small test program (main) managing the point class.


import math 

class Point:
    def __init__(self, x, y):
        # Initializing private variables for the point's coordinates
        self.__x = x
        self.__y = y
    
    def move(self, dx, dy):
        # Moving the point by dx and dy
        self.__x += dx 
        self.__y += dy 

    def display(self):
        # Displaying the point's coordinates
        print(f"({self.__x}, {self.__y})")

    def enter(self):
        # Allowing the user to input new coordinates
        self.__x = float(input("Enter x: "))
        self.__y = float(input("Enter y: "))
    
    def distance(self, other_point):
        # Calculating distance between this point and another point
        return math.sqrt((self.__x - other_point.__x)**2 + (self.__y - other_point.__y)**2)

    def midpoint(self, other_point):
        # Calculating the midpoint between this point and another point
        mid_x = (self.__x + other_point.__x) / 2
        mid_y = (self.__y + other_point.__y) / 2
        return Point(mid_x, mid_y)  # Return a new point for the midpoint


def main():
    # Creating two Point objects
    point1 = Point(2, 3)
    point2 = Point(5, 7)

    # Display the coordinates of both points
    point1.display()  # Display point1
    point2.display()  # Display point2

    # Move point1 by (1, -2) and display the new position
    point1.move(1, -2)
    point1.display()  # Display point1 after movement

    # Calculate and print the distance between point1 and point2
    print(f"Distance between point1 and point2: {point1.distance(point2)}")

    # Find and display the midpoint between point1 and point2
    midpoint = point1.midpoint(point2)
    midpoint.display()  # Display the midpoint (which should be a Point object)

if __name__ == "__main__":
    main()
