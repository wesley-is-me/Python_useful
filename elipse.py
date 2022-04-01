#ask the computer to use the numpy module
import numpy as np 
#ask the computer to use the pyplot funtion from the matplotlib library and assign the variable as plt
import matplotlib.pyplot as plt
#ask the computer to use the matplotlib module, as mpl, the variable for it is mpl
import matplotlib as mpl#
# make a list of numbers, the numbers being every .01 between 0 and 2pi
t = np.arange(0, 2*np.pi, .01)
#Define equations that will be used
x = np.cos(t) * 2
y = np.sin(t)
#Define the color of the axes as "dimgray"
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['dimgray'])
#Define axes
def axes():
    #axes is a line plotted with matplotlib.pyplot at the value y = 0 with the width of the line at .5
    plt.axhline(0, alpha=.5)
    #axes is a line plotted with matplotlib.pyplot at the value x = 0 with the width of the line at .5
    plt.axvline(0, alpha=.5)
# show axes
axes()
# label x axes
plt.xlabel('X Values')
# label y axes
plt.ylabel('Y Values')
# label graph
plt.title("Mathematica Problem 2.9.1")
# show grid
plt.grid(True)
# Combine x and y to be coordinates and color the graph red
plt.plot(x, y, color='red')
# show grid
plt.show()