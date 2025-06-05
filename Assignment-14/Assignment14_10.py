class employee:
    def __init__(self, name, department, salary):
        self.name = name              
        self._department = department 
        self.__salary = salary        

    def showinfo(self):
        print("Name:", self.name)
        print("Department:", self._department)
        print("Salary:", self.__salary)

emp1 = employee("Devashish", "AIML", 100000)
emp1.showinfo()


print("public:", emp1.name)
print("protected:", emp1._department)

