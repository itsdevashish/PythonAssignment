print("Enter a number")
no = int(input())

for i in range(1, no + 1): 
    for j in range(1, i + 1):  
        print(j, end="\t") 
    print() 
