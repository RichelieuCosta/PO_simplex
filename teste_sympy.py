from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Matrix, symbols
import numpy as np

a = symbols('a', extended_real=True)



A = np.array([[-1, 2, 0], [1,-1,0],[3,-10,1]])
# np.matrix(A)
# np.asarray(A)
b = np.array([4, 3])

v = Matrix([[14], [9], [56]])

v[0]+=a
print("olha a matrix v:", v)
np.asarray(A)
b = Matrix(np.asarray(A))
#b = Matrix([[-1, 2, 0], [1,-1,0],[3,-10,1]])

equa = b*v

print(equa)
inequacao = []

inequacao.append((equa[0],">"))
inequacao.append((equa[1],">"))
inequacao.append((equa[2],">"))
inequacao2 = []
inequacao2.append(inequacao)
print(inequacao2)
print(inequacao)
inequacao = [[(equa[0],">"),(equa[1],">"),(equa[2],">")]]
print(inequacao)
#print(reduce_rational_inequalities([[equa[0]>=0, equa[1]>=0, equa[2]>=0]], a))
print(reduce_rational_inequalities(inequacao2, a))
