import os
import shutil
import sys

fname1=sys.argv[1]
fobj=open(fname1,"w")
fobj.write("Devashish is good boy")
fobj.close()


fname2="demo.txt"

copy=shutil.copyfile(fname1, fname2)
print("File copied Done",copy)













