import numpy as np
import sympy as sym
#define symbol
t = sym.Symbol('t')
x = -t
y = t ** 2
Mt = 2 * x * y
Nt = 3 * x - 2 * y
#take differential of x
dx = sym.diff(x)
#take differential of y
dy = sym.diff(y)
#standard equation
f = Mt * dx + Nt * dy
#integrate funtion f between -2 and 1, y can be any variable
y = sym.integrate(f, (t, -2, 1))
print(y)