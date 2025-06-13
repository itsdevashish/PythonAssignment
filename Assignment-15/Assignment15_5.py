import sys
fname= sys.argv[1]
word=sys.argv[2]


fobj=open(fname,"r")
data=fobj.read()
fobj.close()

print("Frequency of word",word,"is",data.count(word))