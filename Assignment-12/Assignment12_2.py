
class circle():
    PI=3.14

    def __init__(self):
        self.radius=0.0
        self.area=0.0
        self.circumferences=0.0
    
    def accept(self):
        self.radius=int(input("Enter Radius of circle : "))
    
    def calculatearea(self):
        self.area=circle.PI*self.radius*self.radius
    
    def calculateCircumference(self):
        self.circumferences=2*circle.PI*self.radius
    
    def display(self):
        print("radius",self.radius)
        print("area",self.area)
        print("Circumference",self.circumferences)


obj1=circle()

obj1.accept()
obj1.calculatearea()
obj1.calculateCircumference()
obj1.display()
        
        


obj2=circle()
obj2.accept()
obj2.calculatearea()
obj2.calculateCircumference()
obj2.display()
