i=1
def Display(no):
    if no<0:
        print("Enter Greater than Zero (0)")
    global i
    if (i<=no):
           j=1
           while(j<=i):
             print("*\t",end="")
             j=j+1
           print()
           i=i+1
           Display(no)

def main():
    Display(5)   

if __name__=="__main__":
    main()