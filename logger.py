from datetime import datetime
from monitor import monitoring
import csv
import time

def logging():

    with open("data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "cpu", "ram"])
        reference_time = datetime.now()
        while (datetime.now() - reference_time).total_seconds() < 60:
            cpu, ram = monitoring()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, cpu, ram])
            time.sleep(0.5)




