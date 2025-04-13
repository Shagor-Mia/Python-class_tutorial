class User:
    def __init__(self,name,email,password) :
        self.name=name
        self._email=email
        self.password=password
        
    def get_email(self):
        return self._email 
       
    def set_email(self,new_email):
       if "@" in new_email: 
         self._email = new_email 
       else:
         print("ther is no email method in new email.")      
    
user1=User("sagor","Sagor@gmail.com","1234")    
user2=User("tamim","tamim@gmail.com","1234")    

print(user1.get_email())
user1.set_email("safwan@gmail.com")
print(user1.get_email())