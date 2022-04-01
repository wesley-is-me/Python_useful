#note that this is problem 32 in our homework for 4.32, try others for fun!

import sympy as sym

 
x = sym.Symbol('x')
y = sym.Symbol('y')
L = sym.Symbol('L')
g = x * y ** 2
f = sym.sqrt(x ** 2 + y ** 2)
c = 54
ggx = sym.diff(g,x)
ggy = sym.diff(g,y)
gfx = sym.diff(f,x)
gfy = sym.diff(f,y)


eq1 = L * ggx - gfx
eq2 = L * ggy - gfy
eq3 = g - c
z = sym.solve((eq1, eq2, eq3), (x, y, L))
n = 0
for sol in z:

    print(f'x = {sol[0]}, y = {sol[1]}')
    
