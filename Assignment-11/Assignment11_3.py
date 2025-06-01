digit_sum = 0
def add(no):
    global digit_sum
    if no != 0:
        temp = no % 10
        digit_sum += temp
        no = no // 10
        add(no)
    return digit_sum

def main():
    result = add(123)
    print(result)

if __name__ == "__main__":
    main()
