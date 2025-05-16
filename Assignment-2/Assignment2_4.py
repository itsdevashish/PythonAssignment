print ("Enter a no")
no=int(input())

sumoffactors=0
result=1
for i in range(1,no):
    if no%i==0:
        sumoffactors= sumoffactors+i

print(sumoffactors)




