
class Animal:
    alive=True
    
class Dog(Animal):
    def speak(self):
        print("woof!")    
        
class Cat(Animal):
    def speak(self):
        print("mewow!")   
        
class Car:
    alive=False
    def speak(self):
        print("boom boom!")        
        
animals=[Dog(),Cat(),Car()] 

for animal in animals:
    animal.speak()  
    print(animal.alive)          