import matplotlib.pyplot as plt
import numpy as np

time_periods = ['T1', 'T2', 'T3', 'T4']
category_a = [20, 35, 30, 35]
category_b = [25, 32, 34, 20]
category_c = [15, 25, 20, 25]

plt.bar(time_periods, category_a, label='Category A', color='skyblue')
plt.bar(time_periods, category_b, bottom=category_a, label='Category B', color='salmon')
bottom_c = np.array(category_a) + np.array(category_b)
plt.bar(time_periods, category_c, bottom=bottom_c, label='Category C', color='lightgreen')

plt.title("Stacked Bar Chart: Category Contribution Over Time")
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.legend()
plt.show()
