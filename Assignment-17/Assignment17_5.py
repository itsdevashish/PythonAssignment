import schedule
import time
import datetime

def task5():
    f = open("Marvellous.txt", "a")
    f.write(str(datetime.datetime.now()) + "\n")
    f.close()

schedule.every(5).minutes.do(task5)

while True:
    schedule.run_pending()
    time.sleep(1)
