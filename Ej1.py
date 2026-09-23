import numpy as np

# 1)
# X = (A + 5)^-1 - 3B
A = np.array([[-6, -3],[0, -3]])
C = np.linalg.inv(A + 5)
B = np.array([[-1, 0], [4, -2]])
X = np.array(C - 3*B)

print(A.shape[0])


#2)
#MATRICES
A = np.array([[1, 2], [0, 2]])
B = np.array([[2, -1], [-1, 5]])
C = np.array([[2, 6], [-1, -0.5]])
I = np.array([[1, 0], [0, 1]])

#check if inverse exists !!!!!!

#(A.C + I)^1
Y = np.linalg.inv(A.dot(C) + I)
#(10I - 3B)
Z = 10*I - 3*B
# X = Y.Z
print(Y.dot(Z))

#DELETE THIS LATER
