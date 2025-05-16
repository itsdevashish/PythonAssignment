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

    
    minimum = data[0]  
    for value in data:
        if value < minimum:
            minimum = value

    print("Maximum number is:", minimum)


if __name__ == "__main__":
    main()
