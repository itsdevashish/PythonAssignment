class student():
    school_name="KVL"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display(self):
        print(self.name)
        print(self.rollno)
        print(student.school_name)

stud1=student("Devashish",1)

print("Enter original")
stud1.display()

print("With edit")
student.school_name="MIP"
stud1.display()