class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def greet(self):
        print(f"the person name is {self.name} and age is {self.age}.") 
        
person=Person("Ali",23)  
person1=Person("sami",27) 

person.greet()  
person1.greet()      
    
           
        