#ask the computer to pull the file "toolkits" from matplotlib(mpl), then use that to access the mplot3d function
from mpl_toolkits import mplot3d
#ask computer to use numpy and remember it as np
import numpy as np
#ask computer to find pyplot in matplot lib and remember it as plt
import matplotlib.pyplot as plt
#ask the computer to use the matplotlib module, as mpl, the variable for it is mpl
import matplotlib as mpl

#plot these axes in 3d
ax = plt.axes(projection='3d')
#pick 100 values between 0 and 2pi and put them in a list
t = np.linspace(0, 2*np.pi, 100)

#define equations
z = t
x = np.cos(t)
y = np.sin(t)

# label x axes
plt.xlabel('X Values')
# label y axes
plt.ylabel('Y Values')
# label z axes
ax.set_zlabel(r'Z Values')
# label graph
plt.title("Mathematica Problem 2.9.3")

#use the plot3d function to put the three values together
ax.plot3D(x, y, z, 'red')
#show graph
plt.show()