import schedule
import time

def task():
    print("Do Coding..!")

schedule.every(30).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
