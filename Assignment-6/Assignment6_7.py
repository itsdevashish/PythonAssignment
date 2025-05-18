print("Enter 5 numbers")
no=5
data=list()

for i in range(no):
    size=int(input())
    data.append(size)

print("Entered elements are :")
for value in data:
    print(value)

print("The Maximum number is :",max(data))


