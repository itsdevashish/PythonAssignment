from functools import reduce
def reducefun(a,b):
    return a*b
    

def main():
    print("Enter no of elemnets")
    size=int(input())

    data=list()

    print("Enter The values :")

    for i in range(size):
        no=int(input())
        data.append(no)
    
    print("Entered elements are :")

    for value in data:
        print(value)
    
    data=reduce(reducefun,data)
    print("Double Data",data)



if __name__ == "__main__":
    main()