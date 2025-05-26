import multiprocessing

def factorial(list):
    for i in list:
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        print("Factorial of", i, "is :", fact)


def main():
    data=[7,5,8,9,10,11,10]
    M1=multiprocessing.Process(target=factorial,args=(data,))
    M1.start()
    M1.join()


if __name__ == "__main__":
    main()
