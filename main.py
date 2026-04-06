from monitor import monitoring
import time

while True:
    cpu, ram = monitoring()
    print(f"CPU Auslastung: {cpu}% | RAM Auslastung: {ram}%")