from abc import ABC,abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print(f"start the car")
    
    def stop(self):
        print(f"stop the car")
        
class Bike(Vehicle):
    def go(self):
        print(f"start the bike")
    
    # def stop(self):
    #     print(f"stop the bike")
        
        
car=Car()  
car.go()
car.stop()  

bike=Bike()