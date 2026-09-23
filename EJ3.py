import numpy as np
import sympy as sp

#Definir punto P
P = sp.Matrix([1, 2, -1])

#Definir normal de los planos de 
n1 = sp.Matrix([2, 1, -1])
n2 = sp.Matrix([1, -1, 1])

#Vector director de la recta 
vd = n1.cross(n2)

print(vd)

#'''
x, y, z, t = sp.symbols('x y z t')

eq1 = sp.Eq(2*x + y - z, 6)
eq2 = sp.Eq(x - y + z, 1)

sol = sp.linsolve([eq1, eq2], (x, y, z))

print(sol)
#'''