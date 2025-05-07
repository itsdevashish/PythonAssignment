def Add(value1,value2):
    ans=value1+value2
    return ans

def main():
    print("Enter 1st Number")
    no1=int(input())

    print("Enter 2nd Number")
    no2=int(input())
    ans=Add(no1,no2)

    print("The Addition is :",ans)

if __name__ == "__main__":
    main()