class Student:
    class_year=2023
    num_student=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.num_student+=1

student1=Student("haji",23)
student2=Student("rakib",25)
student3=Student("rakib",25)


print(Student.class_year)
print(Student.num_student)


        