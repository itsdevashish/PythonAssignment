class employee():

    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    
    def display(self):
        print(self.name)
        print(self.id)
        print(self.salary)

obj1=employee("Devashish",101,50000)

obj1.display()