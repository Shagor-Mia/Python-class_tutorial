
class Car:
    def __init__(self,model,year,color,boolean):
        self.model=model
        self.year=year
        self.color=color
        self.boolean=boolean
        
    def drive(self):
        print(f"drive the {self.model}")
        
    def stop(self):
        print(f"stop the {self.model}")  
        
    def describe(self):
        print(f"{self.model} {self.year} {self.color}")      