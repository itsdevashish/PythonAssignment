import os
import sys
import time
import shutil
import schedule

def DirectoryWatcher(DirectoryName,SecondDirectory,Extension):
    
    flag=os.path.isabs(DirectoryName) 

    if(flag ==False):
         DirectoryName=os.path.abspath(DirectoryName)

    flag=os.path.exists(DirectoryName) 

    if(flag==False):
         print("The path is invalid ")
         exit()
    
    flag=os.path.isdir(DirectoryName) 
    
    if(flag==False):
         print("path is valid but the target is not a directory ")

    if not os.path.exists(SecondDirectory):
        os.mkdir(SecondDirectory)
    for FolderName,SunFolderNames,FileNames in os.walk(DirectoryName):
          for fname in FileNames:
            DFile = os.path.join(FolderName, fname)
            SFile = os.path.join(SecondDirectory, fname)
            if fname.endswith(Extension):
                 shutil.copy(DFile,SFile) 

def main():
        Border="-"*54
        print(Border)
        print("-----------------Marvellous Automation----------------")
        print(Border)
        
        if(len(sys.argv)==2 ):
            if((sys.argv[1]=="--h") or (sys.argv[1]=="--H")):
                print("This application is used to perform Directory Cleaning")
                print("This is the Directory automation script")

            elif((sys.argv[1]=="--u") or (sys.argv[1]=="--U")):
                print("Use the given script as ")
                print("ScriptName.py  NameOfDirectory")
                print("Please provide Valid Absolute path")

        elif(len(sys.argv)==4):
                schedule.every(2).seconds.do(DirectoryWatcher,sys.argv[1],sys.argv[2],sys.argv[3])

                while True:
                    schedule.run_pending()
                    time.sleep(1)
        else:
            print("Invalid number of Command line Arguments")
            print("Use the given flage as :")
            print("--h :Used to Display the help")
            print("--u: Used to Display the Usage")
        
        print(Border)
        print("------------Thank you for using our Script------------")
        print("----------------Marvellous Infosystems----------------")
        print(Border)


if __name__=="__main__":
    main()