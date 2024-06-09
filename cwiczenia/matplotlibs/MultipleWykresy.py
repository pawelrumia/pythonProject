from matplotlib import pyplot as plt
import random

x = [x for x in range(1, 101)]
y_1 = []
y_2 = []

for a in range(0, 100):
    y_1.append(random.randint(1, 101))
    y_2.append(random.randint(1, 101))

plt.plot(x, y_1, 'gx', x, y_2, 'rx')
# plt.show()

plt.subplot(2, 1, 1)
plt.title('Graph1')
plt.plot(x, y_1, 'r')
plt.subplot(2,1,2)
plt.title('Graph2')
plt.plot(x, y_2, 'm')
plt.suptitle('Super Graph')
plt.show()