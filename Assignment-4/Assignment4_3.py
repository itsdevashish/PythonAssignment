from functools import reduce

def filterfun(no):
    if no>=70:
        return no

def mapfun(no):
    return no+10

def reducefun(a,b):
    return a+b

Data=[4,34,36,76,68,24,89,23,86,90,45,70]
print("Input List :",Data)

Fdata=list(filter(filterfun,Data))
print("After Filter List",Fdata)

Mdata= list(map(mapfun,Fdata))
print("After Map List :",Mdata)

Rdata=reduce(reducefun,Mdata)
print("Reduce list is ",Rdata)