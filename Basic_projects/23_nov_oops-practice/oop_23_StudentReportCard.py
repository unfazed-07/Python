class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    
    def calculate_total(self):
        return sum(self.marks.values())
    
    def calculate_percentage(self):
        return (self.calculate_total()/len(self.marks))
    
    def display_report(self):
        print(f"Name: {self.name}")
        print(f"Roll_No: {self.roll_no}")
        for subject, marks in self.marks.items():
            print(f"{subject}: {marks}")
        print(f"\nTotal: {self.calculate_total()}\nPercentage: {self.calculate_percentage()}%\n\n")

class ReportCard:
    def __init__(self):
        self.students = []

    def add_student(self, thatstudent):
        self.students.append(thatstudent)

    def show_all_student_reports(self):
        for student in self.students:
            student.display_report()