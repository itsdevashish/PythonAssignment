def chkpositiveornegative(value1):
    if value1>0:
        print("The Number is Positive")
    
    elif value1==0:
        print("Zero")
    else:
        print("The Number is Negative")


def main():
    print("Enter The Number")
    no=int(input())
    chkpositiveornegative(no)

if __name__ == "__main__":
    main()