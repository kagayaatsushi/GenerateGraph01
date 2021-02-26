import numpy as np
import pandas as pd
import tensorflow as tf
import torch
import keras
import matplotlib.pyplot as plt
import datetime.datetime as dt

x0 = [100, 200, 300, 400, 500]
y0 = [8, 12, 17, 20, 22]

file_name = "resource01_2020226a.txt"
fd = open(file_name, mode='r')
res_lines = fd.readlines()
time = [int(x) for x in (res_lines[0].rstrip('\n').split(','))[1:]]
value1 = [int(x) for x in (res_lines[1].rstrip('\n').split(','))[1:]]
print(time)
print(value1)

plt.plot(time, value1, linestyle="-.", color="blue", marker="d")
plt.savefig("graph01_" + dt.now().strftime('%Y%m%d_%H%M%S') + ".png")
