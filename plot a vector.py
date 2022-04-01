import matplotlib.pyplot as plt
import numpy as np
#move it in the x direction
X = np.array((0))
#move it in the y direction
Y= np.array((0))
#strech it horizontally
U = np.array((2))
#strech it vertically
V = np.array((-2))
#define the ax
fig, ax = plt.subplots()
#use a special function (quiver)
q = ax.quiver(X, Y, U, V,units='xy' ,scale=1)

plt.grid()
#x an y axes are equal
ax.set_aspect('equal')
#What area to show
plt.xlim(-5,5)
plt.ylim(-5,5)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)

plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png') 
plt.show()
