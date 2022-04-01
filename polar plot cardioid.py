import numpy as np
import matplotlib.pyplot as plt
import math
  
  
# setting the axes
# projection as polar
plt.axes(projection = 'polar')
  
#seting the parts of the equation
a = 3
b = -2
# creating an array
# containing the radian values
rads = np.arange(0, (2 * np.pi), 0.01)
   
# plotting the cardioid
for rad in rads:
    r = a + (b*np.cos(rad)) 
    plt.polar(rad,r,'g.') 
  
# display the polar plot
plt.show()