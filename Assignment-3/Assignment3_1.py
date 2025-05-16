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

    total = 0
    for value in data:
        total = total + value  # or total += value

    print("Total sum of all elements:", total)


if __name__ == "__main__":
    main()
