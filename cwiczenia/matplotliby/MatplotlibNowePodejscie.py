from matplotlib import pyplot as plt
import random

x = [x for x in range(1, 101)]
y = []
for i in range(100):
    y.append(random.randint(1, 101))

wykres = plt.plot(x, y)
# plt.scatter(x, y)
plt.xlabel('Time (s)')
plt.ylabel('Temperature (degC)')
# plt.show()
plt.setp(wykres, linewidth=3, color='g')
plt.show()