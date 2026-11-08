from person import Teacher, Person, Student
from school import School


class Subject:
    def __init__ (self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam (self, students):  # students = list of student
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grade[self.name] = School.value_to_grade (mark)
            