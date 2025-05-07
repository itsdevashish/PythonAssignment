def ChkNum(no):
    if no%2==0 :
        print("Even Number") 
    else:
        print("Odd Number")
    
    return no

def main():
    print("Enter Number")
    value1= int(input())
    ChkNum(value1)

if __name__=="__main__":
    main()