class Dog:
    def __init__(self,name, bark,owner):
        self.name=name
        self.bark=bark
        self.owner=owner
        
    def Bark(self):
        print("woof")
class Owner:
    def __init__(self,name,address,contact):
        self.name=name
        self.address=address
        self.contact=contact
        
owner1=Owner("sagor","homna","1234556")
owner2=Owner("sanji","homna","1234556")
                
dog1=Dog("kallu","ghewu ghwu",owner1)   

print(dog1.owner.name)
dog1.Bark()  

dog2=Dog("maallu","ghewu ghwu ghu",owner2)   
print(dog2.name,dog2.bark,)
dog2.Bark()     