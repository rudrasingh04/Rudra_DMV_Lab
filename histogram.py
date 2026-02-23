import matplotlib.pyplot as plt

data = [10, 12, 15, 20, 22, 22, 25, 30, 30, 30, 35]

plt.hist(data)

plt.title("Basic Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()
