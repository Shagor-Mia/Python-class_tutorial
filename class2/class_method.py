class Student:
    student=0
    total_gpa=0
    
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.student+=1
        Student.total_gpa+=gpa
        
    
    def student_info(self):
        return f"Student name is {self.name} and GPA: {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total student : {cls.student}"  
    
    @classmethod
    def avg_gpa(cls):
        if cls.student==0:
         return 0
     
        return f"Average GPA of students :{cls.total_gpa/cls.student:.2f}"  
    
student1=Student("sagor",3.23)  
student2=Student("anis",3.00)    
student3=Student("tamim",3.05)    

print(student1.student_info())  

# print(Student.student)
print(Student.get_count())
print(Student.avg_gpa())

