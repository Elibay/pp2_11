class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print(self):
        print(self.name, self.age)


class Student(Person):
    # def __int__(self, age, name, gpa):
    #     super(Student, self).__init__(age, name)
    #     self.age = age
    #     self.name = name
    #     self.gpa = gpa
    gpa = 3.0

    def set_gpa(self, gpa):
        self.gpa = gpa

    def print(self):
        print(self.name, self.age, self.gpa)


a = Person(17, "Azamat")
a.print()
b = Student(20, "Aybol")
b.gpa = 3.99
b.print()
