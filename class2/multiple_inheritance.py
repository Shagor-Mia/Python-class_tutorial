class Prey:
    def flee(self):
        print("this animal is  fleeing")

class Predator:
    def hunt(self):
        print("this animal is  hunting")

class Hawk(Predator):
    pass

class Rabbit(Prey):
    pass

class Fish(Prey,Predator):
    pass

hawk=Hawk()
rabbit=Rabbit()
fish=Fish()

fish.flee()