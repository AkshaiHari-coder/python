class Student:
    def __init__(self, rollno, name, course):
        self.rollno = rollno
        self.name = name
        self.course = course

class Test(Student):
    def __init__(self, rollno, name, course, marks):
        super().__init__(rollno, name, course)
        self.marks = marks

class Result(Test):
    def calculateGrade(self):
        if self.marks > 480:
            grade = "Distinction"
        elif self.marks > 360:
            grade = "First Class"
        elif self.marks > 240:
            grade = "Second Class"
        else:
            grade = "Failed"

        print("\n--- Result ---")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total Marks:", self.marks)
        print("Grade:", grade)


r = int(input("Enter Roll Number: "))
n = input("Enter Name: ")
c = input("Enter Course Name: ")
m = int(input("Enter Marks (out of 600): "))

stud = Result(r, n, c, m)
stud.calculateGrade()
