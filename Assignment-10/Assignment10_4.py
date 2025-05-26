from functools import reduce

def filterfun(no):
    if no%2==0:
        return no
    
def mapfun(no):
    return no*no

def reducefun(a,b):
    return a+b

Data=[5,2,3,4,3,4,1,2,8,10]
print("The Inputr List is :",Data)

Fdata=list(filter(filterfun,Data))
print(Fdata)

Mdata=list(map(mapfun,Fdata))
print(Mdata)

Rdata=reduce(reducefun,Mdata)
print(Rdata)