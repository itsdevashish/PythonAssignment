import threading

def small(s):
    count=0
    for i in s:
        if i.islower():
            count=count+1
    print(count)

def capital(s):
    count=0
    for i in s:
        if i.isupper():
            count=count+1
    print(count)

def digit(no):
    count=0
    for i in no:
        if i.isdigit():
            count=count+1
    print(count)

t1=threading.Thread(target=small,args=("potnis",))
t2=threading.Thread(target=capital,args=("POTNIS",))
t3=threading.Thread(target=digit,args=("12345678",))

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
