class book():

    def __init__(self,price):
        self.__price=price
    
    def getprice(self):
        return self.__price
    
    def setprice(self,new_price):
        self.__price = new_price


b1 = book(500)
print("Initial Price:", b1.getprice())
b1.setprice(600)
print("Updated Price:", b1.getprice())



