import os
import sys
import time
import hashlib
import schedule

def CalculateCheckSum(path, BlockSize=1024):
    fobj = open(path, "rb")
    hobj = hashlib.md5()
    buffer = fobj.read(BlockSize)
    while len(buffer) > 0:
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)
    fobj.close()
    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName="AutoScan"):
    flag = os.path.isabs(DirectoryName)
    if flag == False:
        DirectoryName = os.path.abspath(DirectoryName)
    flag = os.path.exists(DirectoryName)
    if flag == False:
        print("The path is invalid")
        exit()
    flag = os.path.isdir(DirectoryName)
    if flag == False:
        print("Path is valid but the target is not a directory")

    Files = {}
    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):
        for fname in FileNames:
            fname = os.path.join(FolderName, fname)
            checksum = CalculateCheckSum(fname)
            if checksum in Files:
                Files[checksum].append(fname)
            else:
                Files[checksum] = [fname]
    CreateLog(Files)

def CreateLog(Files):
    Dir = "LogFiles"
    if not os.path.exists(Dir):
        os.makedirs(Dir)
    timestamp = time.ctime()
    fileName = os.path.join(Dir, "AutoLog %s.log" % timestamp)
    fileName = fileName.replace(" ", "_").replace(":", "_")

    fobj = open(fileName, "w")
    Border = "-" * 54
    fobj.write(Border + "\n")
    fobj.write("This is a log file of Directory Automation Script\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(Border + "\n")

    for checksum, filepaths in Files.items():
        fobj.write("Checksum: " + checksum + "\n")
        for path in filepaths:
            fobj.write("   File: " + path + "\n")
        fobj.write("\n")

    fobj.write(Border + "\n")
    fobj.write("File created at :\n" + timestamp + "\n")
    fobj.write(Border + "\n")

def main():
    Border = "-" * 54
    print(Border)
    print("-----------------Directory Automation Tool----------------")
    print(Border)

    if len(sys.argv) == 2:
        if sys.argv[1] in ("--h", "--H"):
            print("This application is used to perform Directory Cleaning")
            print("This is the Directory Automation Script")
        elif sys.argv[1] in ("--u", "--U"):
            print("Use the given script as:")
            print("ScriptName.py  NameOfDirectory")
            print("Please provide a valid absolute path")
        else:
            schedule.every(3).seconds.do(DirectoryWatcher, sys.argv[1])
            while True:
                schedule.run_pending()
                time.sleep(1)
    else:
        print("Invalid number of command-line arguments")
        print("Use the following flags:")
        print("--h : Used to display help")
        print("--u : Used to display usage")

    print(Border)
    print("------------Thank you for using our Script------------")
    print("---------------------AutoSoft--------------------------")
    print(Border)

if __name__ == "__main__":
    main()
