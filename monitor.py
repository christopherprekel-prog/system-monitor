import psutil

def monitoring():
    cpu_load = psutil.cpu_percent(interval=1)
    ram_load = psutil.virtual_memory().percent
    return cpu_load, ram_load