#ask the computer to use the numpy module
import numpy as np
#ask the computer to use the matplotlib module, as mpl, the variable for it is mpl
import matplotlib as mpl
#ask the computer to use the pyplot funtion from the matplotlib library and assign the variable as plt
import matplotlib.pyplot as plt
#Define the color of the axes as "dimgray"
mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['dimgray'])#
#ask the computer to make a list of 400 evenly plotted points between -6 and 8 and assign them to the variable of x
x = np.linspace(-6, 8, 400)
#ask the computer to make a list of 400 evenly plotted points between -10 and 14 and assign them to the variable of y
y = np.linspace(-10, 14, 400)
#Put the x and the y plots together.
x, y = np.meshgrid(x, y)
# define the function "axes"  
def axes():
    #axes is a line plotted with matplotlib.pyplot at the value y = 0 with the width of the line at .5
    plt.axhline(0, alpha=.5)
    #axes is a line plotted with matplotlib.pyplot at the value x = 0 with the width of the line at .5
    plt.axvline(0, alpha=.5)
# define variable values
H = 1
K = 2
A = 5
B = 9
# show axes
axes()
# Equation to plot,#1, with color purple (#1.Determines the number and positions of the contour lines / regions.If an int n, use n data intervals; i.e. draw n+1 contour lines. The level heights are automatically chosen. If array-like, draw contour lines at the specified levels. The values must be in increasing order.)
plt.contour(x, y,((x-H)**2/A - (y-K)**2/B), [1], colors='purple')
# label x axes
plt.xlabel('X Values')
# label y axes
plt.ylabel('Y Values')
# label graph
plt.title("Mathematica Problem 2.8")
# show grid
plt.grid(True)
# show graph
plt.show()