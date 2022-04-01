import numpy as np
import matplotlib.pyplot as plt
  
  
# setting the axes
# projection as polar
plt.axes(projection='polar')
  
# setting the length
# and number of petals
a = 5
n = 2
  
# creating an array
# containing the radian values
rads = np.arange(0, 2 * np.pi, 0.001) 
  
# plotting the rose
for rad in rads:
    r = a * np.sin(n*rad)
    plt.polar(rad, r, 'g.')
   
# display the polar plot
plt.show()