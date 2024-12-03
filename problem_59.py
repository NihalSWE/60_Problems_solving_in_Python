# Exercise 59
# 1. Define a Book class with the following attributes: Title, Author (Full Name), Price.
# 2. Define a constructor with the following attributes: Title, Author, Price.
# 3. Define the View() method to display the information of a Book object instance.
# 4. Write a program to test the Book class.

# Question 1
class Book:
     # Question 2
     def __init__(self, Title, Author, Price):
          self.Title     = Title
          self.Author    = Author
          self.Price     = Price
         
     # Question 3
     def view(self) :
          return ("Book Title: ",  self.Title  , "Book Author: ",  self.Author , "Book Price: ",  self.Price )
         
# Question 4
MyBook = Book("Python" , "Mohamed" , "23 Dh")         
print(  MyBook.view ())