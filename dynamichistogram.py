import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    data = np.random.randn(1000)  # Generate random data
    ax.hist(data, bins=30, color='blue', alpha=0.7)
    ax.set_xlim(-5, 5)
    ax.set_ylim(0, 200)
    ax.set_title("Dynamic Histogram")

ani = FuncAnimation(fig, update, interval=500)

plt.show()