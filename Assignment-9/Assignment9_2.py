import multiprocessing
import multiprocessing.process


def square(data):
    for i in data:
        print(i*i)

def main():
    data=[1,2,3,4,5,6,7,8,9,10,11,12]
    m1=multiprocessing.Process(target=square,args=(data,))
    m2=multiprocessing.Process(target=square,args=(data,))
    m3=multiprocessing.Process(target=square,args=(data,))
    
    m1.start()
    m2.start()
    m3.start()

    m1.join()
    m2.join()
    m3.join()

  


if __name__ == "__main__":
    main()

