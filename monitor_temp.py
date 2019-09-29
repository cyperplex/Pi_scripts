import os
import time
import logging

#Simple Script to monitor PI temp and write to log

def measure_temp():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

while True:
        try:
           dt_str = time.strftime("%d/%m/%Y %H:%M:%S")
           print("date and time =", dt_str)
           print("Current Temperature: ", measure_temp())
           logging.info("Current Temp: ", measure_temp())
           time.sleep(60)
        except IOError as e:
            print(e)
            logging.critical('Error Temp Script Failure')
