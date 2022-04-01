import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import numpy as np
from numpy import sin, cos, pi


ax = plt.figure().add_subplot(projection='3d')

# Make data.
X = np.arange(-6, 6, 0.25)
xlen = len(X)
Y = np.arange(-6, 6, 0.25)
ylen = len(Y)
X, Y = np.meshgrid(X, Y)

Z = X ** 2 + Y + 4

# Create an empty array of strings with the same shape as the meshgrid, and
# populate it with two colors in a checkerboard pattern.
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]

# Plot the surface with face colors taken from the array we made.
surf = ax.plot_surface(X, Y, Z, facecolors=colors, linewidth=0, alpha = .5)


# Customize the z axis.
ax.set_zlim(0, 35)
ax.zaxis.set_major_locator(LinearLocator(6))
#turn path into a parametric equation
#my xyz now ghi so it doesn't mess with the stuff above and height
# is equal to the  x and y plugged into original
t = np.linspace(0, 2 * pi, 400)
g = 5 * cos(t)
h = 5 * sin(t)
i = (g ** 2) + (h) + 4
plt.plot(g, h, i, 'g', linewidth = 4)
plt.title("Problem 4.21")
plt.show()














plt.show()

