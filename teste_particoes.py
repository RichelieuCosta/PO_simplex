import numpy as np


def atualizeBN(A, I_b, I_n):
    B = []
    N = []

    for linhaA in A:
        linhaB = []
        linhaN = []
        for j in I_b:
            print(j)
            linhaB.append(linhaA[j-1])
            print(linhaB)
        B.append(linhaB)
        for j in I_n:
            print(j)
            linhaN.append(linhaA[j-1])
            print(linhaN)
        N.append(linhaN)

    return B, N


def obter_particoes_iniciais(A, b):

    len(A)
    I_b = np.zeros((len(A)), dtype=int)
    I_n = np.zeros((len(A[1])-len(A)), dtype=int)

    x_x_b = []  # solução_avaliada
    x_x_b = np.multiply(np.linalg.inv(B), b)

    return I_b, I_n


A = [[1, 1, 1, 0, 0],
     [1, -1, 0, 1, 0],
     [3, 1, 0, 0, -1]]

for l in A:
    print(l)

b = [6, 4, 3]
I_b = []  # indice das variáveis que estão na partição básica
I_n = []  # indice das variáveis que estão na partição não básica
# A_inv = []
print("ola")

I_b = [1, 2, 5]
I_n = [3, 4]
#I_b, I_n = obter_particoes_iniciais(A, b)
print("partições básicas:", I_b)
print("partições não básicas:", I_n)

B, N = atualizeBN(A, I_b, I_n)
print("Saiu da função de atualização de BN")

print("matriz Básica:")
for l in B:
    print(l)

print("matriz não básica")
for l in N:
    print(l)

x_x_b = []  # solução_avaliada
x_x_b = np.multiply(np.linalg.inv(B), b)


""".git\A = [] # matrix_Ax
A = matriz[:][:-1]
b = []
b = matriz[:][len(matriz[1])-1]

I_b = [] #indice das variáveis que estão na partição básica
I_n = [] #indice das variáveis que estão na partição não básica
A_inv = []

I_b, I_n=obter_particoes(A, b)


B = [] #Matrix_Básica
print(B.T)

m # numero de equações
n # número de variáveis
#resolvendo sistema de equações lineares:
#Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2:
#a = np.array([[1, 2], [3, 5]])
#b = np.array([1, 2])
#x = np.linalg.solve(a, b)
#x

N = [] # matrix_NãoBásica
a_n = [] # a_n[] são as colunas de N
x = []

if x_x_b >= 0:
    print("solução básica viável")
Lambda = [] # vetor multiplicador simplex

c = [] # vetor de custos
c_b = []  # vetor de coeficientes das variáveis básicas
c_n = [] # vetor de coeficientes das variáveis não básicas
c_xapeu_n = c_n[:] - np.multiply(Lambda.T,a_n[:]) # custos relativos não básicos
y = [] # direção do simplex
y[:] = np.multiply(np.linalg.inv(B),N[:]) # Errado. quero pegar as colunas de N
c_xapeu_k = [] # teste de otimalidade nas não básicas
 min{c_n}
E_xapeu = []
E_xapeu[:] = x_x_b[:]/y[:]
# np.linalg.inv(B)

"""

""".git\A = [] # matrix_Ax
A = matriz[:][:-1]
b = []
b = matriz[:][len(matriz[1])-1]

I_b = [] #indice das variáveis que estão na partição básica
I_n = [] #indice das variáveis que estão na partição não básica
A_inv = []

I_b, I_n=obter_particoes(A, b)


B = [] #Matrix_Básica
print(B.T)

m # numero de equações
n # número de variáveis
#resolvendo sistema de equações lineares:
#Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2:
#a = np.array([[1, 2], [3, 5]])
#b = np.array([1, 2])
#x = np.linalg.solve(a, b)
#x

N = [] # matrix_NãoBásica
a_n = [] # a_n[] são as colunas de N
x = []
x_x_b = [] # solução_avaliada
x_x_b = np.multiply(np.linalg.inv(B),b)
if x_x_b >= 0:
    print("solução básica viável")
Lambda = [] # vetor multiplicador simplex

c = [] # vetor de custos
c_b = []  # vetor de coeficientes das variáveis básicas
c_n = [] # vetor de coeficientes das variáveis não básicas
c_xapeu_n = c_n[:] - np.multiply(Lambda.T,a_n[:]) # custos relativos não básicos
y = [] # direção do simplex
y[:] = np.multiply(np.linalg.inv(B),N[:]) # Errado. quero pegar as colunas de N
c_xapeu_k = [] # teste de otimalidade nas não básicas
 min{c_n}
E_xapeu = []
E_xapeu[:] = x_x_b[:]/y[:]
# np.linalg.inv(B)

"""
