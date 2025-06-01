Rec=1
Sum=0
def Display(no):
    global Rec
    global Sum
    if(Rec<=no):
        Sum=Sum+Rec
        Rec=Rec+1
        Display(no)
    return Sum

def main():
    Ret=Display(5)
    print("Sum of Number :",Ret)
   

if __name__=="__main__":
    main()