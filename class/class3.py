class User:
    def __init__(self,name,email,password) :
        self.name=name
        self.email=email
        self.password=password
        
    def send_hi_to_user(self,user):
        print(f"hi:{user.name}.this is me {self.name}")    
        
user1=User("sagor","sagor@gmail.com","1234")    
user2=User("tamim","tamim@gmail.com","1234")    

user1.send_hi_to_user(user2)