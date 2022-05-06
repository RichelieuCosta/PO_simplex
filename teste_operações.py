import numpy as np

A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])


b = np.array([120, 40, 30])

print(A)
print(b)
# print(A.dot(b))

# Binv = np.linalg.inv(np.matrix(B))
# x_x_b = []  # solução_avaliada
b_t = np.matrix(b)
print(b_t)

print(np.matrix(b).dot(A))


c = np.arange(5)

c += 1

print(c)
