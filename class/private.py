class User:
    def __init__(self,name,email,password) :
        self.name=name
        self.__email=email
        self.password=password
        
    def clean_email(self):
        return self.__email.lower().strip()    
        
    
user1=User("sagor"," Sagor@gmail.com ","1234")    
user2=User("tamim","tamim@gmail.com","1234")    

print(user1.__email)
print(user1.clean_email())