import psutil

def process_display():
    border = "*" * 50
    print(border)
    print("Information of Currently Running Processes")
    print(border)

    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        info = proc.info
        print(info)

def main():
    process_display()

if __name__ == "__main__":
    main()
