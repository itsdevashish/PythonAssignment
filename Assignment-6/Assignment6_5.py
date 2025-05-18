print("Enter a number")
no=int(input())

for i in range(2,no):
    if (no%2==0):
        print(no,"is a not prime number")
        break
else:
    print(no,"is a prime number")