import schedule
import time

def check_mail():
    print("Checking mail...")

schedule.every(10).seconds.do(check_mail)

while True:
    schedule.run_pending()
    time.sleep(1)
