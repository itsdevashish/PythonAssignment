class numbers():
    def __init__(self, no):
        self.no = no
    
    def chkprime(self):
        count = 0
        for i in range(1, self.no + 1):
            if self.no % i == 0:
                count += 1
        if count == 2:
            return True
        else:
            return False

    def factors(self):
        for i in range(1, self.no):
            if self.no % i == 0:
                print(i)

    def sumfactors(self):
        total = 0
        for i in range(1, self.no):
            if self.no % i == 0:
                total += i
        return total  


obj1 = numbers(28)
print("Factors are:")
obj1.factors()

print("prime no :", obj1.chkprime())
print("sum of factors:", obj1.sumfactors())
