import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Create circle
circle = plt.Circle((0, 5), 0.5, color='blue')
ax.add_patch(circle)

def update(frame):
    circle.center = (frame, 5)
    return circle,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 10, 100),
                    interval=30, blit=True)

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Moving Circle Animation")
plt.show()