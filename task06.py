class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def __str__(self):
        return f"{self.name}, {self.age} yoshda, {self.grade} - sinf o'quvchisi."


t1 = Student("Ali", 20, 9)


print(t1)
