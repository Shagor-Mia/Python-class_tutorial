from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass    
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return self.radius*3.1416
                
class Square(Shape):
   def __init__(self,width):
        self.width=width
   def area(self):
        return self.width**2
        
class Trinlge(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return f"area of a tringle{self.width*self.width*0.5:.2f}"    
        
shapes=[Circle(3),Square(5),Trinlge(3,5)]   

for shape in shapes:
    print(shape.area())            
                
                      
                       
                              