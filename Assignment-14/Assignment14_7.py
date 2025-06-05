class baseperson():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    

class derivedteacher(baseperson):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary=salary

d1=derivedteacher("Devashish",23,"Math",23000)
print("Name is :",d1.name)
print("Age is :",d1.age)
print("Subject is :",d1.subject)
print("Salary is :",d1.salary)