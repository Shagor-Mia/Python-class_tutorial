class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f" {self.name} is eating")
        
    def sleep(self):
        print(f" {self.name} is sleeping")    


class Prey(Animal):
    def flee(self):
        print(f" {self.name} is  fleeing")

class Predator(Animal):
    def hunt(self):
        print(f" {self.name} is  hunting")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

hawk=Hawk("bugs")
rabbit=Rabbit("tony")
fish=Fish("nemo")

fish.sleep()