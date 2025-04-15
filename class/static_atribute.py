
class User:
    user_count=0
    
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password
        User.user_count+=1
        
user1=User("sagor","sagor@gmail.com","1234")    
user2=User("tamim","tamim@gmail.com","1234")       

# print(User.user_count)
print(user1.user_count)
print(user2.user_count)

