class School:
    def __init__ (self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}   # {"bangla" = teacher_object}
        self.classrooms = {}  # {"nine" = classroom_object}

    def add_classroom (self, classroom): # in this method "classroom" is object
        self.classrooms[classroom.name] = classroom

    def add_teacher (self, subject, teacher): # in this method "teacher" is obsect
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)


    @staticmethod
    def calculate_grade (marks):
        if (marks >= 80 and marks <= 100):
            return 'A+'
        elif marks >= 70 and marks < 80:
            return 'A'
        elif marks >= 60 and marks < 70:
            return 'A-'
        elif marks >= 50 and marks < 60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_value (grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]

    
    @staticmethod 
    def value_to_grade (value):
        if (value >= 4.5 and value <= 5.00):
            return 'A+'
        elif value >= 3.5 and value < 4.50:
            return 'A'
        elif value >= 3.00 and value < 3.50:
            return 'A-'
        elif value >= 2.50 and value < 3.00:
            return 'B'
        elif value >= 2.00 and value < 2.50:
            return 'C'
        elif value >= 1.00 and value < 2.00:
            return 'D'
        else:
            return 'F'

    def __repr__ (self) -> str:
        # all classrooms
        for key in self.classrooms.keys():
            print (key)

        # all students
        print ("All Students")
        result = ''
        for key, value in self.classrooms.items ():
            result += f'--------{key.upper()} Classroom Students\n'
            for student in value.students:
                result += f'{student.name}\n'
        print (result)

        # all subjects
        print ("\nAll Subjects")
        subject = ''
        for key, value in self.classrooms.items():
            subject += f'-------{key.upper()} Classroom Subject\n'
            for sub in value.subjects:
                subject += f'{sub.name}\n'
        print (subject)

        # all teachers
        print ("\nAll Teachers")
        for key, value in self.teachers.items():
            print (f"Subject Name: {key.upper()} -> Teacher Name: {value.name}\n")


        # all Student's results
        print ("\nStudents Results")
        for key, value in self.classrooms.items ():
            for st in value.students:
                for i, v in st.marks.items():
                    print (st.name, i, v, st.subject_grade[i])
                print (st.calculate_final_grade ())
        
        return ""