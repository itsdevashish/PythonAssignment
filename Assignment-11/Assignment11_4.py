Result = 1  

def power(no, pow):
    global Result
    if pow > 0:
        Result = Result * no
        pow = pow - 1
        power(no, pow)
    return Result

def main():
    global Result
    Result = 1  
    ret = power(2, 3)  
    print(ret)

if __name__ == "__main__":
    main()
