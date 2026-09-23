import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# definir la variable
a = sp.symbols('a')

# definir la matriz
M = sp.Matrix([
    [1, 1, -1],
    [3, a, a],
    [4, a, 0]
])

# definir terminos independientes
b = sp.Matrix([
    [1],
    [5],
    [5]
])

# calcular determinante
det_M = M.det()

print("Detereminante: ", det_M, '\n')

# obtener valores de a
solutions = sp.solve(det_M, a)
print("Soluciones para a: ", solutions, '\n')

for i in range(len(solutions)):
    M_sub = M.subs(a, solutions[i])
    rank = M_sub.rank()

    M_amp = M_sub.row_join(b)
    rank_amp = M_amp.rank()

    if rank != rank_amp:
        print("SI cuando a =", solutions[i]) 
    else:
        print("SCI cuando a =", solutions[i], " de grado ", 3-rank)

print("Para a != ", solutions, 'SCD')

'''
# Plano 1 a=0
n1 = np.array([1,1,-1])
D1 = 1
X, Y = np.meshgrid(range(10), range(10))
Z1 = (-n1[0]*X - n1[1]*Y - D1) / n1[2]

# Planos verticales
Y2, Z2 = np.meshgrid(range(10), range(10))

X2 = np.full_like(Y2, 5/3)   # 3x = 5
X3 = np.full_like(Y2, 5/4)   # 4x = 5

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, alpha=0.5, color='blue')
ax.plot_surface(X2, Y2, Z2, alpha=0.5, color='red')
ax.plot_surface(X3, Y2, Z2, alpha=0.5, color='green')

plt.show()
'''

# Plano a = 5
n1 = np.array([1,1,-1])
n2 = np.array([3,5,5])
n3 = np.array([4,5,0])

D1 = 1
D2 = 5
D3 = 5

X, Y = np.meshgrid(np.linspace(-20, 20, 50), np.linspace(-20, 20, 50))

# Planes that can solve for z
z1 = (-n1[0]*X - n1[1]*Y - D1) / n1[2]
z2 = (-n2[0]*X - n2[1]*Y - D2) / n2[2]

# For plane 3 (solve for x instead)
Z = np.meshgrid(range(10), range(10))[0]  # reuse grid
X3 = (-n3[1]*Y - D3) / n3[0]

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot_surface(X, Y, z1, color="blue")
ax.plot_surface(X, Y, z2, color="red")

# Plot vertical plane
ax.plot_surface(X3, Y, Z, color="green")

#ax.scatter(point[0], point[1], point[2], color='black', s=50)

plt.show()
