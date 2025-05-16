def main():
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

    
    maximum = data[0]  
    for value in data:
        if value > maximum:
            maximum = value

    print("Maximum number is:", maximum)


if __name__ == "__main__":
    main()
