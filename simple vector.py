import matplotlib.pyplot as plt
import numpy as np

X = np.array((0))
Y= np.array((0))
U = np.array((2))
V = np.array((-2))

fig, ax = plt.subplots()
q = ax.quiver(X, Y, U, V,units='xy' ,scale=1)

plt.grid()

ax.set_aspect('equal')

plt.xlim(-5,5)
plt.ylim(-5,5)

plt.title('How to plot a vector in matplotlib ?',fontsize=10)

plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')
plt.show()
#plt.close()