import math
import numpy
import matplotlib.pyplot as matp

a = 7
x = math.sin(a)
print(x)
y = numpy.tan(a)
print(y)

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

z = [5, 2, 4, 4, 8, 7, 4, 8, 10, 9]

matp.plot(v, z)
matp.xlabel('Time (s)')
matp.ylabel('Temparute (degC)')
matp.show()
