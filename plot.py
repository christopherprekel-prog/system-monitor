import matplotlib.pyplot as plt
from datetime import datetime
import csv

def plot_cpu_ram():

    timestamps = []
    cpu_values = []
    ram_values = []

    with open("data.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            timestamps.append(row[0])
            cpu_values.append(float(row[1]))
            ram_values.append(float(row[2]))

    t = []
    for iterator in timestamps:
        t.append(datetime.strptime(iterator, "%Y-%m-%d %H:%M:%S"))

    reference_time = t[0]
    x_axis = []
    for iterator in t:
        x_axis.append((iterator - reference_time).total_seconds())

    plt.plot(x_axis, cpu_values, label="CPU")
    plt.plot(x_axis, ram_values, label="RAM")
    plt.legend()
    plt.grid()
    plt.savefig("RAM_CPU_Plot.pdf")