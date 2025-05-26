import threading
import time

def displayno(no):
    for i in range(1,no+1):
        print(i)
        time.sleep(1)

T1=threading.Thread(target=displayno,args=(5,))
T2=threading.Thread(target=displayno,args=(5,))
T3=threading.Thread(target=displayno,args=(5,))

T1.start()
T2.start()
T3.start()

T1.join()
T2.join()
T3.join()


