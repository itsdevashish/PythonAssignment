import os
import sys
import filecmp



file1=sys.argv[1]
file2=sys.argv[2]


fobj=open(file1,"w")
fobj.write("Devahsish is good boy")



fobj2=open(file2,"w")
fobj2.write("Devahsish is good boy")


if filecmp.cmp(file1, file2, shallow=False):
         print("Files are same.")
else:
         print("Files are different.")