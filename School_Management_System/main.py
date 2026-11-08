from school import*
from person import*
from subject import*
from classroom import*

school = School ("ABC", "Rajshahi")

eight = ClassRoom ("Eight")
nine = ClassRoom ("Nine")
ten = ClassRoom ("Ten")

school.add_classroom (eight)
school.add_classroom (nine)
school.add_classroom (ten)

# adding Student
rahim = Student ("Rahim", eight)
korim = Student ("Korim", nine)
fahim = Student ("Fahim", ten)
hamim = Student ("Hamim", eight)

school.student_admission (rahim)
school.student_admission (korim)
school.student_admission (fahim)
school.student_admission (hamim)

# adding Teacher
abdullah = Teacher ("Abdullah")
abdurrahman = Teacher ("Abdurrahman")
abduloyahid = Teacher ("Abdul Oyahid")

bangla = Subject ("Bangla", abdullah)
physics = Subject ("Physice", abdurrahman)
chemistry = Subject ("Chemistry", abduloyahid)
biology = Subject ("Biology", abduloyahid)


eight.add_subject (bangla)
eight.add_subject (physics)
eight.add_subject (chemistry)
nine.add_subject (biology)
nine.add_subject (chemistry)
nine.add_subject (physics)
ten.add_subject (chemistry)
ten.add_subject (physics)
ten.add_subject (bangla)
ten.add_subject (biology)

eight.take_semester_final_exam ()
nine.take_semester_final_exam ()
ten.take_semester_final_exam ()

print (school)