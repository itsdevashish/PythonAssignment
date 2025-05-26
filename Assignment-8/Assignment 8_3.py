import threading

def evenlist(no):
    sum=0
    for i in no:
        if i%2==0:
            sum=sum+i
    print(sum)

def oddlist(no):
    sum=0
    for i in no:
        if i%2!=0:
            sum=sum+i
    print(sum)



data=[10,57,87,3,50]


t1=threading.Thread(target=evenlist,args=(data,))
t2=threading.Thread(target=oddlist,args=(data,))


t1.start()
t2.start()

t1.join()
t2.join()





