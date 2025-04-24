class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
        
    def get_info(self):
        return f"emloyee name {self.name} and position {self.position}"   
    
    @staticmethod
    def valid_info(position):
       valid_position=["manager","hr","chef"] 
       return position in valid_position
   
print(Employee.valid_info("hr"))

employee1=Employee("sagor","admin")
employee2=Employee("sunny","hr")

print(employee1.get_info())
print(employee2.get_info())


   