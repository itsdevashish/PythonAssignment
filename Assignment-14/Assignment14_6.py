class calculator():
    
    def __init__(self):
        self.value1=0
        self.value2=0

    def accept(self):
        self.value1=int(input("Enter first number : "))
        self.value2=int(input("Enter second number : "))

    def addition(self):
        return self.value1+self.value2
    
    def substraction(self):
         return self.value1-self.value2
    
    def multiplication(self):
        return self.value1*self.value2
    
    def division(self):
        return self.value1/self.value2
    
obj1=calculator()
obj1.accept()
print("Addition is :",obj1.addition())
print("Addition is :",obj1.substraction())
print("Addition is :",obj1.multiplication())
print("Addition is :",obj1.division())


obj2=calculator()
obj2.accept()
print("Addition is :",obj2.addition())
print("Addition is :",obj2.substraction())
print("Addition is :",obj2.multiplication())
print("Addition is :",obj2.division())