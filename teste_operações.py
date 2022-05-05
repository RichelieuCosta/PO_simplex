import numpy as np

A = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])


b = np.array([120, 40, 30])

print(A.dot(b))
