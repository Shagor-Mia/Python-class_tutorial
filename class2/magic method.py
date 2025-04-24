class Book:
    
    def __init__(self,title,author,num_page):
        self.title=title
        self.author=author
        self.num_page=num_page
    
    def __str__(self):
        return f"author of {self.title} is {self.author}."   
    
    def __eq__(self,other):
        return self.title == other.title and self.author==other.author
    
    def __lt__(self,other):
        return self.num_page < other.num_page
    
    def __gt__(self,other):
        return self.num_page > other.num_page
    
    def __add__(self,other):
        return f"{self.num_page + other.num_page} pages" 
    
    def __contains__(self,keyword):
        return keyword in self.author or self.title
    
    def __getitem__(self,key):
        if key=="title":
            return self.title
        elif key=="athor":
            return self.author
        elif key=="page":
            return self.num_page
        return "not the correct key!"
    
book1=Book("chuti","tagor",223)
book0=Book("chuti","tagor",222)

book2=Book("chol chol","kazi nazrul islam",223)        
book3=Book("dukhu","kazi",223)  

print(book1) 
print (book1==book0)
print (book0<book1)     
print (book0>book1) 
print (book0+book1)     
print ("islam" in book3)  
print (book3["pag"])     
   
    
     
        