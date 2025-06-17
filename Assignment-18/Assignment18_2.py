import os

fname=input("Enter file name :")

if os.path.exists(fname):
    print("File is availabe")

    fobj=open(fname,"r")

    content=fobj.read()
    print(content)
    fobj.close()
else:
    print("File is not available")