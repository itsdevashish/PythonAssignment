import psutil
import sys

def process_display(process_name):
    border = "*" * 50
    print(border)
    print(f"Information of running process: {process_name}")
    print(border)

    found = False
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        if proc.info['name'].lower() == process_name.lower():
            print(f"PID      : {proc.info['pid']}")
            print(f"Name     : {proc.info['name']}")
            print(f"User     : {proc.info['username']}")
            print(border)
            found = True

    if not found:
        print(f"No process found with name: {process_name}")
        print(border)

def main():
    if len(sys.argv) != 2:
        print("Usage: ProcInfo.py <ProcessName>")
        sys.exit(1)

    process_name = sys.argv[1]
    process_display(process_name)

if __name__ == "__main__":
    main()
