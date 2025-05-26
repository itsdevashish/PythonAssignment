import threading

def evendisplay(no):
    for i in range(1,no+1):
        if (i%2==0):
            print(i)

def odddisplay(no):
    for i in range(1,no+1):
        if (i%2!=0):
            print(i)


t1=threading.Thread(target=evendisplay,args=(10,))
t1.start()

t2=threading.Thread(target=odddisplay,args=(10,))
t2.start()