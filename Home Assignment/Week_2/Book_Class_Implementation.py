'''

Assignment Details:
Create a Python class named Book with the following:
 Attributes: title, author, and publication_year.
 A method get_age() that calculates and returns the age of the book in years (current year
– publication_year).
Requirements:
 Define a class named Book.
 Use the __init__ method to initialize attributes.
 Define the get_age() method inside the class.
 Create an object of the Book class and call the method to display the book’s age.
Hints to Solve:
 Use the datetime module to get the current year.
 Subtract publication_year from the current year to find the age.
 Example structure:
import datetime
class Book:
def __init__(self, title, author, publication_year):
self.title = title
self.author = author
self.publication_year = publication_year
def get_age(self):
current_year = datetime.datetime.now().year
return current_year - self.publication_year

'''



from datetime import datetime

class Book:

    def __init__(self,Author, title,Publication_Year):
        self.Author = Author
        self.title = title
        self.Publication_Year=Publication_Year


    def get_age(self):
        Book_age = datetime.now().year - self.Publication_Year
        return Book_age
        
    

book1= Book("Subash","How do i love you",2005)
age = book1.get_age()
print("Book Age is",age )




        
        


