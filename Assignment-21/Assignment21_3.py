import os
import psutil
import time
import sys

def create_log(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    log_filename = f"ProcessLog_{time.strftime('%Y%m%d_%H%M%S')}.txt"
    log_path = os.path.join(directory, log_filename)

    with open(log_path, 'w') as f:
        f.write("*" * 50 + "\n")
        f.write("Process Log Created on: " + time.ctime() + "\n")
        f.write("*" * 50 + "\n\n")

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            info = proc.info
            f.write(f"PID: {info['pid']}, Name: {info['name']}, User: {info['username']}\n")

    print(f"\n Log file created successfully")

def main():
    if len(sys.argv) != 2:
        print("Usage: ProcInfoLog.py <DirectoryName>")
        return

    directory = sys.argv[1]
    create_log(directory)

if __name__ == "__main__":
    main()
