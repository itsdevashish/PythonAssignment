
power=lambda a:a**a

def main():
    print ("Enter a number")
    no=int(input())

    answer=power(no)

    print("The Power of",no,"is",answer)

if __name__ =="__main__":
    main()