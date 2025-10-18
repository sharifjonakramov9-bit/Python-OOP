class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


s1 = Student("Ali", 12)
s2 = Student("Vali", 13)
s2 = Student("Aziz", 14)
s3 = Student("Sobir", 15)
s4 = Student("Sherzod", 16)
s5 = Student("Doni", 17)
s6 = Student("Temur", 18)

students = [s1, s2, s3, s4, s5, s6]

mx = max(students, key=lambda e: e.age)

mx.show_info()
