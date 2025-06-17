import os

fname=input("Enter File name :")

if os.path.exists(fname):
    print("Your file is availabe")
else:
    print("File is not availabe")
