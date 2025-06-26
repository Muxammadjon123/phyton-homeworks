import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'orange', 'purple']

for i in range(len(products)):
    plt.bar(products[i], sales[i], color=colors[i])

plt.title("Sales Data by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()
