print("Enter first number")
no=int(input())

fact=1
for i in range(1,no+1):
    fact=fact*i
print("The factorial of",i,"is :",fact)