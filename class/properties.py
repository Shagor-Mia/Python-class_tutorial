class User:
    def __init__(self,name,email,password) :
        self.name=name
        self._email=email
        self.password=password
    
    # getter property
    @property
    def email(self):
        print("email accessed.")
        return self._email    
    # setter property
    @email.setter
    def  email(self,new_email):
        if "@" in new_email: 
         self._email = new_email 
        
user1=User("sagor","sagor@gmail.com","1234")    
   

user1.email="this is not email."
print(user1.email)