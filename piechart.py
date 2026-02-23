import matplotlib.pyplot as plt

labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
sizes = [30, 25, 20, 25]
colors = ['red', 'yellow', 'pink', 'brown']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.title('Fruit Distribution')

plt.show()