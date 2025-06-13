f = open("numbers.txt", "w")
for i in range(10):
    n = input("Enter number: ")
    f.write(n + "\n")
f.close()