class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students =[]

    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value/len(self.students)

s1 = Student("Tim", 20, 95)
s2 = Student("Jim", 25, 86)
s3 = Student("Bill", 24, 80)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.students[0].age)
print(course.get_average_grade())

# class method
class Person:
    no_of_person = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def no_of_person_(cls):
        return cls.no_of_person

    @classmethod
    def add_person(cls):
        cls.no_of_person +=1


p1 = Person("tim")
p2 = Person("bill")
print(Person.no_of_person_())

# Staticmethod
class Math:

    @staticmethod
    def add5(x):
        return x + 5

print(Math.add5(5))