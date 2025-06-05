class rectangle():

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width
    
    def parameter(self):
        return (self.length+self.width)*2
    
cret=rectangle(50,50)

print(cret.area())
print(cret.parameter())