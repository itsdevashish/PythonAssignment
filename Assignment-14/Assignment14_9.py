class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price


p1 = product("Laptop", 10000)
p2 = product("Phone", 10000)
p3 = product("Tablet", 3000)

print(p1 == p2)  
print(p1 == p3)  
