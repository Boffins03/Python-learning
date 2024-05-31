class School:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name, age, status, rank):
        self.name = name
        self.age = age
        self.status = status
        self.rank = rank

class Class:
    def __init__(self, class_number, section):
        self.class_number = class_number
        self.section = section

class Student(School, Class):
    def __init__(self, name, age, class_number, section, subjects):
        School.__init__(self, name)
        Class.__init__(self, class_number, section)
        self.age = age
        self.subjects = subjects

    def get_info_of_student(self):
        print(f"Name of the student is {self.name}, age is {self.age}, "
              f"and he/she is in class {self.class_number}-{self.section}. "
              f"Subjects: {', '.join(self.subjects)}")


# Creating an instance of the Student class
student1 = Student("Huzaifa", 21, 12, 'A', ["Hindi", "English", "Maths", "Physics", "Chemistry"])
student1.get_info_of_student()
