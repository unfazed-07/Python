from oop_23_StudentReportCard import *
total_students = int(input("Enter the number of Students: "))
rc = ReportCard()
for i in range(total_students):
    name = input("Enter a student name")
    roll_no = input("Enter Roll No.")
    marks = {}
    marks["Physics"]=int(input("Marks for Physics: "))
    marks["Chemistry"]=int(input("Enter chemistry marks: "))
    marks["Maths"]=int(input("Enter maths marks: "))

    s1=Student(name, roll_no, marks)
    rc.add_student(s1)

rc.show_all_student_reports()