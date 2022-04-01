import sympy as sym
import numpy as np
from matplotlib import pyplot as py
 
t = sym.Symbol('t')
#if you wanted to graph this equation like the problem asked un comment stuff
#t = np.arange( 0, 4, .01)
#t = sym.pi / 4
x = 2 * sym.cos(t)
y = 3 * sym.sin(t)
 
z = (9 - (x ** 2) - (y ** 2))
dr = sym.diff(z)
#Up to this point python made an equation, to get it to plug a value into that funtion 
# you have to subsitute like this.
z = dr.subs(t, sym.pi/4)

print(z)
#py.grid(True)
#py.plot(t, z, color='red')

#py.show()