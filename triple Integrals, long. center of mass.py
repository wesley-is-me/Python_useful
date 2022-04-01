import numpy as np
import sympy as sym
t = sym.Symbol('t')
x = sym.Symbol('x')
z = sym.Symbol('z')
y = sym.Symbol('y')

z1 = sym.integrate(y, (z, 0, 10 - 2 * x))
y1 = sym.integrate(z1, (y, 0, 7))
x1 = sym.integrate(y1, (x, 0, 5))
z2 = sym.integrate(1, (z, 0, 10 - 2 * x))
y2 = sym.integrate(z2, (y, 0, 7))
x2 = sym.integrate(y2, (x, 0, 5))
print(x1/x2)