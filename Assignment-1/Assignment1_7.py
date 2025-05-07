def chkdivisible(value1):
    if value1 %5==0:
        print("True")
    else:
        print("False")    
    
def main():
    print("Enter The Number To Check")
    no1=int(input())
    chkdivisible(no1)

if __name__ =="__main__":
    main()   