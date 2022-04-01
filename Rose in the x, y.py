import numpy as np
import sympy as sym
import matplotlib as mpl
import matplotlib.pyplot as plt
a = 5
n = 2
t = np.arange(0, 2 * np.pi, .01)
r = a * np.sin(n*t) 
x = r * np.cos(t)
y = r * np.sin(t)
plt.grid()
plt.plot(x, y)
plt.show()