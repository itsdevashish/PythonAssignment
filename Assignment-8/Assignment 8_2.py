import threading

def evendisplay(no):
    sum=0
    for i in range(1,no+1):
        if(no%i==0):
            if (i%2==0): 
                sum=sum+i
    print(sum)

def odddisplay(no):
    odd_sum = 0
    for i in range(1, no+1):
        if (no % i == 0): 
            if (i % 2 != 0): 
                odd_sum =odd_sum+i
    print(odd_sum)

print("Enter a number ")
no=int(input())

t1=threading.Thread(target=evendisplay,args=(no,))
t2=threading.Thread(target=odddisplay,args=(no,))

t1.start()
t2.start()

t1.join()
t2.join()