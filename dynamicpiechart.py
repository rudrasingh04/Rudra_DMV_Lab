import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

labels = ['A', 'B', 'C', 'D']

def update(frame):
    ax.clear()
    data = np.random.randint(1, 10, size=4)
    ax.pie(data, labels=labels, autopct='%1.1f%%')
    ax.set_title("Dynamic Pie Chart")

ani = FuncAnimation(fig, update, interval=1000)

plt.show()