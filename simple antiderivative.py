import numpy as np
import sympy as sym
x = sym.Symbol('x')
#standard equation
f = 7 * x + 5
#integrate funtion f between -2 and 1, y can be any variable
y = sym.integrate(f)
print(y)