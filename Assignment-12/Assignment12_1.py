
class demo():
    value=0 #class variable
    
    def __init__(self,no1,no2): #-> instance variable
        self.no1=no1
        self.no2=no2

    def fun(self): #Instance method
        print(self.no1)
        print(self.no2)
    
    def gun(self): # Instance method
            print(self.no1)
            print(self.no2)

    
obj1=demo(11,21)
obj2=demo(51,101)

obj1.fun()
obj2.gun()


    