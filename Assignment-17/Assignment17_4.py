import schedule
import time

def fun():
    print("Namaskar...")

schedule.every().day.at("09:00").do(fun)

while True:
    schedule.run_pending()
    time.sleep(1)
