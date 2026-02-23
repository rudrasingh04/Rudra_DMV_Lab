import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]

plt.step(x, y)

plt.title("Basic Stair Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()