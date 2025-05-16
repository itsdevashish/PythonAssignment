from MarvellousNum import ChkPrime

def ListPrime():
    print("Enter number of elements:")
    size = int(input())

    data = []

    print("Enter the values:")

    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Entered elements are:")
    for value in data:
        print(value)

    total = 0
    print("Prime numbers are:", end=" ")
    for value in data:
        if ChkPrime(value):
            total += value
            print(value, end=" ")

    print("\nSum of prime numbers:", total)


if __name__ == "__main__":
    ListPrime()
