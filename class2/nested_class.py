
class Company:
    
    class Employee:
        def __init__(self,name,position):
         self.name=name
         self.position=position
         
        def get_details(self):
            return f"name of employee {self.name} and position is {self.position}" 
    
    def __init__(self,company_name):
        self.company_name=company_name
        self.employees=[]
        
    def add_employee(self,name,position):
        new_employee=self.Employee(name,position)
        self.employees.append(new_employee)
    
    def list_employee(self):
        return [employee.get_details() for employee in self.employees]
    
company1=Company('Pran')  
company2=Company('incepta')    
  

company1.add_employee('hanif',"manager")
company1.add_employee('sohan',"HR")
company1.add_employee('kabir',"admin")

company2.add_employee('muktar',"cook")
company2.add_employee('sunny',"cashier")

# print(company.list_employee())

for employee in company1.list_employee():
    print(employee)
    
for employee in company2.list_employee():
    print(employee)    

    
            