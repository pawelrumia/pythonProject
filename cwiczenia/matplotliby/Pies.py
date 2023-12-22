import matplotlib.pyplot as plt
pie_chart = {'Patison': 38, "Jasiulenka": 6, 'Pawel': 39}
plt.pie(pie_chart.values(), labels=pie_chart.keys(), explode=(0.1, 0.0, 0.0), shadow=True, startangle=90)
plt.show()