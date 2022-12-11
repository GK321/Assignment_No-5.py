# Problem statement
# Implement the complete Student class by completing the tasks below.

class student:
    studentlist = []
    def add_student(self):
        print("           Add students          ")
        student_name = (input("Enter student Name : "))
        student_roll_number = int(input("Enter Roll Number : "))
        student = student(student_name= student_name, student_roll_number= student_roll_number)
        self.studentlist.append(student)
        print("Student Information Successfully!!!")


    def __init__(self,name, roll_number):
        self.roll_number = roll_number
        
    def __str__(self):
        return f"student details : \nname: {self.name} \nroll_number: {self.roll_number}"

    #setter for student

    def self_name(self,name):
        self.name = name

    #getter for student
    def get_name(self):
        return self.name
    
    #setter for student
    def self_roll_number(self,roll_number):
        self.roll_number = roll_number

    #getter for student
    def get_roll_number(self):
        return self.roll_number

    def view_student(self):
        for i  in self.studentlist:
            print(self.studentlist)

