# School Management System

A simple object-oriented school management system built in Python to manage students, teachers, classrooms, subjects, and academic results.

## Overview

This project demonstrates how a school can be modeled using classes and relationships between core entities such as:

- School
- Classroom
- Student
- Teacher
- Subject
- Person

It is designed for educational purposes and helps model basic school operations such as:

- Student admission
- Classroom assignment
- Teacher registration
- Subject assignment
- Semester exam simulation
- Grade calculation
- Final result generation

## Features

- Add classrooms to a school
- Admit students into their class
- Assign subjects to classrooms
- Register teachers for subjects
- Simulate exam marks
- Convert marks into grade letters
- Calculate GPA and final grade
- Display school, classroom, subject, and student result information

## Project Structure

```text
School_Management_System/
├── classroom.py
├── main.py
├── person.py
├── school.py
├── subject.py
├── README.md
```

## Class Design

### Person
Base class for all people in the system.

### Teacher
Represents a teacher and can evaluate exam marks.

### Student
Represents a student and stores:
- name
- classroom
- marks
- subject grades
- final grade

### ClassRoom
Represents a classroom and contains:
- class name
- students
- subjects

### Subject
Represents an academic subject and handles exam simulation.

### School
Represents the entire school and manages:
- classrooms
- teachers
- student admissions

## Grade Calculation

The system uses a grade mapping for subject marks:

- 80–100: A+
- 70–79: A
- 60–69: A-
- 50–59: B
- 40–49: C
- 33–39: D
- Below 33: F

It also converts grade points to letter grades and calculates an average GPA for final evaluation.

## Prerequisites

Before running the project, ensure that you have:

- Python 3.8 or above installed
- A Linux/macOS/Windows terminal
- Basic understanding of Python classes and object-oriented programming

## Installation

Clone or download the project to your local machine:

```bash
cd /home/mim-mozahid/Desktop/01_phitron/Restaurant_Management_System
```

Navigate to the project directory:

```bash
cd School_Management_System
```

## Running the Application

Execute the main script:

```bash
python3 main.py
```

If your system uses `python` instead of `python3`, use:

```bash
python main.py
```

## Example Workflow

The application creates:

- multiple classrooms
- several students
- various subjects
- teachers for those subjects

Then it:

1. Admits students to classrooms
2. Adds subjects to classrooms
3. Runs exam simulation
4. Stores subject marks
5. Converts marks to grades
6. Calculates final grade/GPA
7. Prints the school result summary

## Example Output

The application prints information such as:

- available classrooms
- students enrolled in each class
- subjects in each classroom
- teachers assigned to subjects
- student marks and grades
- final GPA and overall result

## Notes

This project is structured as a simple academic demonstration of Python OOP principles, including:

- encapsulation
- inheritance
- composition
- static methods
- dictionaries and lists
- data modeling

## Future Enhancements

Potential improvements for the system include:

- Add student ID generation with better validation
- Add subject-specific passing criteria
- Implement file-based data storage using JSON or CSV
- Add user authentication for admin/teacher roles
- Add a terminal-based admin dashboard
- Add GUI support with Tkinter or Flask
- Support multiple semesters and academic years

## License

This project is intended for educational and learning purposes. No official license is included unless specified by the repository owner.

## Author

Developed as a learning project for object-oriented programming in Python.

## Summary

This School Management System is a beginner-friendly Python project that models real-world school operations using clean class-based architecture. It is suitable for understanding how OOP can be applied to build a practical management application.