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

    print("Enter the element to search:")
    search_element = int(input())

    frequency = 0
    for value in data:
        if value == search_element:
            frequency += 1

    print("Frequency of", search_element, "is:", frequency)


if __name__ == "__main__":
    main()
