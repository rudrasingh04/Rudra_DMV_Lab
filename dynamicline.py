import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x_data = []
y_data = []
line, = ax.plot([], [], color='blue')

ax.set_xlim(0, 50)
ax.set_ylim(-1.5, 1.5)

def update(frame):
    x_data.append(frame)
    y_data.append(np.sin(frame * 0.1))
    line.set_data(x_data, y_data)
    return line,

ani = FuncAnimation(fig, update, frames=np.arange(0, 50),
                    interval=100, blit=True)

plt.title("Dynamic Line Graph")
plt.show()