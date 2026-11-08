import random
from school import School


class Person:
    def __init__ (self, name):
        self.name = name

    
class Teacher (Person):
    def __init__ (self, name):
        super().__init__ (name)

    def evaluate_exam (self):
        return random.randint (1, 100)


class Student (Person):
    def __init__ (self, name, classroom):
        super().__init__ (name)
        self.classroom = classroom
        self.__id = None
        self.marks = {} # {"bangla" : 78, "english" = 81} => store like this
        self.subject_grade = {} # {"english" = "A+"} -> store like this
        self.grade = None  # final grade

    
    def final_grade (self):
        sum = 0.00
        for grade in self.subject_grade.values():
            point += School.grade_to_value (grade)
            sum += point

        gra = sum / len (self.subject_grade)
        self.grade = School.value_to_grade (gra)


    @property
    def id (self):
        return self.__id

    @id.setter
    def id (self, value):
        self.__id = value
