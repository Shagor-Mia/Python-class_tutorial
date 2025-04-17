
class Library:
    def __init__(self,name):
        self.name=name
        self.books=[]
    def add_books(self,book):
        self.books.append(book)   
    def list_books(self):
        return [f"{book.title} by {book.author} " for book in self.books]    
        
class Books:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        
library=Library("Dhaka library.")
   
book1=Books("Marvel","stan lee") 
book2=Books("dc","worner bros")             
book3=Books("disney"," disneep")             
            
library.add_books(book1)            
library.add_books(book2)            
library.add_books(book3)   


for book in library.list_books():
    print(book)         
