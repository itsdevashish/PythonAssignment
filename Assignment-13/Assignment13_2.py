class bankaccount():
    ROI=10.5

    def __init__(self,name,amount):
        self.name=name
        self.amount=amount
    
    def deposit(self):
        deposit_amount = int (input("Enter Deposit amount :"))
        self.amount += deposit_amount

    def withdraw(self):
        withdraw_amount = int(input("Enter withdraw amount: "))
        if withdraw_amount <= self.amount:
            self.amount -= withdraw_amount
        else:
            print("Insufficient balance.")

    def calculate_interest(self):
        interest = (self.amount * bankaccount.ROI) / 100
        print(f"Interest: ₹{interest}")

    def display(self):
        print(f"Name: {self.name}, Amount: ₹{self.amount}")


acc1 = bankaccount("Devashish",10000)
acc1.deposit()
acc1.withdraw()
acc1.calculate_interest()
acc1.display()
