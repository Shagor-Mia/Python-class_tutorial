class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True
        
    def eat(self):
        print(f"{self.name} is eating.")    
        
    def sleep(self):
        print(f"{self.name} is sleeping.") 
        
class Dog(Animal):
    def speak(self):
        print("woof!")

class Cat(Animal):
    def speak(self):
        print("mew!")

class Mouse(Animal):
    def speak(self):
        print("squeek!")

dog= Dog("scoby")
cat= Dog("tomy")
mouse= Dog("jerry")


print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()   

dog.speak()        
           