import matplotlib.pyplot as plt


plt.subplot(1, 2, 1)   # (rows, columns, position)
plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Plot 1")


plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [6, 5, 4])
plt.title("Plot 2")

plt.tight_layout()
plt.show()