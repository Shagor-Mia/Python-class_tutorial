class Shape:
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled
        
    def describe(self):
        print(f"it is {self.color} and {'filled' if self.is_filled else'not filled'}")
            
        
class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius
        
    def describe(self):
        print(f"the area of a circle is {3.1416*self.radius:.2f}")   
        super().describe()
                
class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)
        self.width=width 
    def describe(self):
        print(f"the area of a square is {self.width*self.width:.2f}")   
        super().describe()     
        
class Trinlge(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)
        self.width=width  
        self.height=height 
    def describe(self):
        print(f"the area of a tringle is {self.width*self.height/2:.2f}")   
        super().describe()        
        
circle=Circle(color="red",is_filled=True,  radius=7)    
square=Square(color="blue",is_filled=False,width=3)     
tringle=Trinlge(color="green",is_filled=True,width=2,height=4)      

print(circle.color,circle.is_filled,circle.radius)  
circle.describe()  

square.describe()
tringle.describe()                
                
                      
                       
                              