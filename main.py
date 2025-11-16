# notes version 0.1.0
import datetime
import time

while True:
    now = datetime.datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S") 
    print(current_time)
    with open("time.txt", "a") as time_file:
        time_file.write(current_time+"\n")
    time.sleep(60)
