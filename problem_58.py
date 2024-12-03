# Exercise 58 
# Code a myString class that allows you to provide strings with append() and pop() methods that do the same operations as lists. Example: if you create strings via the instantiation s1 = myString("Hello") and s2 = "hello", and you apply the methods:
# print( s1.append ("world!")) # displays 'Hello world!' 
# print( s2.pop (2)) # displays 'hello'.Exercise 58 


class myString:
    def __init__(self,s):
        self.s=s

    def append(self,x):
        self.s += x
        return self.s 
    def pop(self, y):
        self.s=self.s[:-y]
        return self.s

s1 = myString("Hello")
print(s1.append(" world!")) # displays 'Hello world!'
s2 = myString("hello")
print(s2.pop(2)) # displays 'hel!'
