class Student :
    def __init__ (self, student_name , student_marks):
        self.name = student_name
        self.marks = student_marks

    def display(self):
        print(f"Name : {self.name}, Marks : {self.marks}")   

student1 = Student ("Iraj Fatima" , 98)     

student1.display()
