# Exercise 47  : Sum class 


# Write  in Python  a “Sum” class having two variables “n1” and “n2” and a member function “som()” which calculates the sum. In the main main method ask the user to enter two integers and pass them to the default constructor of the "Sum" class and display the result of adding the two numbers.

class Sum:
    def __init__(self, n1,n2):
        self.X=n1
        self.Y=n2
    
    def sum(self):
        return  self.X + self.Y
    
if  __name__ == '__main__':
    n1=int(input("Enter the first number : "))
    n2=int(input("Enter the second number : "))
    s=Sum(n1,n2)
    print(f"The sum is {s.sum()}")