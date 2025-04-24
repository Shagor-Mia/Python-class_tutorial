class Engine:
    def __init__(self,horse_power):
        self.horse_power=horse_power
        
class Wheel:
    def __init__(self,size):
        self.size=size
        
class Car:
    def __init__(self,make,model,horse_power,wheel_size):
        self.model=model
        self.make=make
        self.engine=Engine(horse_power)
        self.wheels=[Wheel(wheel_size) for wheel in range(4)] 
        
    def display(self):
        return f"car is{self.make} and {self.model} power {self.engine.horse_power} tyre size {self.wheels[0].size}"      
        
        
car1=Car("ford","mustang",12,4)
car2=Car("toyota","corolla",22,6)                     
car3=Car("nissan","thunder",14,8)    

print(car1.display())                 
                     