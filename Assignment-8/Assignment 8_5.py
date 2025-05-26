import threading
def thread1(no):
    for i in range(1,no+1):
        print(i)

def thread2(no):
    for i in range(no,0,-1):
        print(i)

t1=threading.Thread(target=thread1,args=(50,))
t2=threading.Thread(target=thread1,args=(50,))

t1.start()
t2.start()

t1.join()
t2.join()
