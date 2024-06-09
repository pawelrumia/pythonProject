from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

x = [x for x in range(1, 101)]
y_1 = []
y_2 = []

for a in range(0, 100):
    y_1.append(random.randint(1, 101))
    y_2.append(random.randint(1, 101))

axes = plt.axes(projection='3d')
axes.scatter3D(x, y_1, y_2)
plt.show()