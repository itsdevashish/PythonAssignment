import threading
import multiprocessing

def summing(no):
    total=0
    for i in range(1,no+1):
        total=total+i
    print(total)

def main():

    summing(10000000)

    T1=threading.Thread(target=summing,args=(10000000,))
    T1.start()

    M1=multiprocessing.Process(target=summing,args=(10000000,))
    M1.start()


    T1.join()
    M1.join()

if __name__ == "__main__":
    main()
