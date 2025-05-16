import Arithmetic
def main():
    print("Enter First Numner")
    no1=int(input())

    print("Enter Second Number")
    no2=int(input())

    answer=Arithmetic.Add(no1,no2)
    print("The addition is :", answer)

    answer=Arithmetic.Sub(no1,no2)
    print("The Substraction is :", answer)

    answer=Arithmetic.Mult(no1,no2)
    print("The Multiplication is :", answer)

    answer=Arithmetic.Div(no1,no2)
    print("The Division is :", answer)

if __name__ == "__main__":
    main()