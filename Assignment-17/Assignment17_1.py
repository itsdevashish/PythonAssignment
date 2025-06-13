import schedule
import time

def fun():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(fun)

while True:
    schedule.run_pending()
    time.sleep(1)
