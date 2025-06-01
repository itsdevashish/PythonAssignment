def factorial(no):
    fact=1

    while(no >= 1):
        fact=fact*no
        no=no-1

    return fact

def main():
    ret=factorial(5)
    print(ret)

if __name__=="__main__":
    main()