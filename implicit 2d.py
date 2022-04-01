from matplotlib import pyplot as plt
import numpy as np
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
delta = 0.025

#you may have to change these to fit the situation
xrange = np.arange(-2.0, 2.0, delta)
yrange = np.arange(-2.0, 2.0, delta)

x, y = np.meshgrid(xrange, yrange)

#change this to whatever you need it to implicit plot in 2d
equation = x ** 2 + y ** 2 - 1

plt.grid()
plt.contour(x, y, equation, [0])
plt.show()