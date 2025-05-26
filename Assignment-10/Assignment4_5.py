from functools import reduce

def filterfun(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True 

def mapfun(no):
    return no*2

def reducefun(a,b):
    if a > b:
        return a
    else:
        return b


Data=[2,70,11,10,17,23,31,77]
print("The Input List is :",Data)

Fdata =list(filter(filterfun,Data))
print(Fdata)

Mdata=list(map(mapfun,Fdata))
print(Mdata)

Rdata=reduce(reducefun,Mdata)
print(Rdata)