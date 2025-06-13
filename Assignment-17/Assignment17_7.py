import schedule
import time
from datetime import datetime

def task():
    f = open("Marvellous.txt", "a")
    f.write(str(datetime.now()) + "\n")
    f.close()

schedule.every(5).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
