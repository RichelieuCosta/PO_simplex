import numpy as np


def atualizeBN(A, I_b, I_n):
    B = []
    N = []

    for linhaA in A:
        linhaB = []
        linhaN = []
        for j in I_b:
            # print(j)
            linhaB.append(linhaA[j-1])
            # print(linhaB)
        B.append(linhaB)
        for j in I_n:
            # print(j)
            linhaN.append(linhaA[j-1])
            # print(linhaN)
        N.append(linhaN)

    return np.asarray(B), np.asarray(N)


def obter_particoes_iniciais(A, b):

    len(A)
    I_b = np.zeros((len(A)), dtype=int)
    I_n = np.zeros((len(A[1])-len(A)), dtype=int)

    x_x_b = []  # solução_avaliada
    x_x_b = np.multiply(np.linalg.inv(B), b)

    return I_b, I_n


A = np.array([[1, 1, 1, 0, 0],
              [1, -1, 0, 1, 0],
              [3, 1, 0, 0, -1]])

for l in A:
    print(l)

b = np.array([6, 4, 3])
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

print("b:", np.matrix(b).getT())
print("matriz Básica:")
print(B)

print("matriz não básica")
print(N)
Binv = np.linalg.inv(np.matrix(B))

print(Binv)
x_x_b = []  # solução_avaliada
x_x_b = Binv.dot(np.matrix(b).getT())

if x_x_b.all() >= 0:
    print("Conjunto legal!!")

print(x_x_b)

""".git\A = np.zeros( (1,1) ) # matrix_Ax
A = matriz[:][:-1]
b = np.arange(1)
b = matriz[:][len(matriz[1])-1]

I_b = np.arange(1) #indice das variáveis que estão na partição básica
I_n = np.arange(1) #indice das variáveis que estão na partição não básica
A_inv = np.zeros( (1,1) )

I_b, I_n=obter_particoes(A, b)


B = np.zeros( (1,1) ) #Matrix_Básica
print(B.T)

m # numero de equações
n # número de variáveis
#resolvendo sistema de equações lineares:
#Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2:
#a = np.array([[1, 2], [3, 5]])
#b = np.array([1, 2])
#x = np.linalg.solve(a, b)
#x

N = np.zeros( (1,1) ) # matrix_NãoBásica
a_n = np.arange(1) # a_n[] são as colunas de N
x = np.arange(1)

if x_x_b >= 0:
    print("solução básica viável")
Lambda = np.arange(1) # vetor multiplicador simplex

c = np.arange(1) # vetor de custos
c_b = np.arange(1)  # vetor de coeficientes das variáveis básicas
c_n = np.arange(1) # vetor de coeficientes das variáveis não básicas
c_xapeu_n = c_n[:] - np.multiply(Lambda.T,a_n[:]) # custos relativos não básicos
y = np.arange(1) # direção do simplex
y[:] = np.multiply(np.linalg.inv(B),N[:]) # Errado. quero pegar as colunas de N
c_xapeu_k = np.arange(1) # teste de otimalidade nas não básicas
 min{c_n}
E_xapeu = np.arange(1)
E_xapeu[:] = x_x_b[:]/y[:]
# np.linalg.inv(B)

"""
