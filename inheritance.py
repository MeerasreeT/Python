class School:
    class Student:
        def __init__(self, name, roll_no):
            self.name = name
            self.roll_no = roll_no

    def __init__(self, school_name):
        self.school_name = school_name
        self.students = []  

    def add_student(self, name, roll_no):
        student = self.Student(name, roll_no)
        self.students.append(student)  

    def display(self):
        print("School Name: ",self.school_name)
        print("Students:")
        for student in self.students:
            print("Name:",student.name," Roll Number:", student.roll_no)


a = School("Star School")
a.add_student("Meera", 2201)
a.add_student("Saranya", 2202)
a.add_student("Saran", 2203)

a.display()
