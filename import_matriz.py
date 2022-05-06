from ctypes import c_bool
from imp import is_builtin
import numpy as np
arq = open('arquivo.txt', 'r')  # abre o arquivo
texto = []  # declaro um vetor
matriz = []  # declaro um segundo vetor
texto = arq.readline()  # quebra as linhas do arquivo em vetores
print("vetor texto -> ", texto)  # aqui eu mostro
c_t = []
c_t.append(np.array(texto))
c_t = np.matrix(c_t)

A = []
texto = arq.readline()  # quebra as linhas do arquivo em vetores
print("vetor texto -> ", texto)  # aqui eu mostro
texto = arq.readline()
while texto != '\n':
    A.append(np.array(texto.split()))
    texto = arq.readline()

A = np.matrix(A)
print(A)

texto = arq.readline()

b = []
b = np.matrix(texto)

c = b[0]
print(c)
"""
print("vetor texto -> ", texto)
print(texto == '\n')
print("")

for i in range(len(texto)):  # esse for percorre a posições do vetor texto
    # aqui eu quebro nos espasos das palavras
    matriz.append(np.array(texto[i].split()))

# print("vetor matriz -> ", matriz)  # mostra o vertor com um conjunto de vetores
# print("")
matriz = np.matrix(matriz)
print(" matriz -> ")  # mostra o vertor com um conjunto de vetores
print(matriz)

matrizA = []
matrizA = np.delete(matriz, 0, 0)

print(matrizA)
matrizB = np.delete(matriz, 2, 0)
print(matrizB)
matrizC = np.delete(matrizA, len(matrizA)-1, 0)
print(matrizC)

arq.close()  # comando para fechar o arquivo


def obter_particoes(A, b):

    return I_b, I_n


def primal_simplex(A, x, b, c):

    return x_x_b
# variavéis que precisarei:


"""

"""
A = []  # matrix_Ax
A = matriz[:][:-1]
b = []
b = matriz[:][len(matriz[1])-1]

I_b = []  # indice das variáveis que estão na partição básica
I_n = []  # indice das variáveis que estão na partição não básica
A_inv = []

I_b, I_n = obter_particoes(A, b)


B = []  # Matrix_Básica
print(B.T)

m  # numero de equações
n  # número de variáveis
# resolvendo sistema de equações lineares:
# Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2:
# a = np.array([[1, 2], [3, 5]])
# b = np.array([1, 2])
# x = np.linalg.solve(a, b)
# x

N = []  # matrix_NãoBásica
a_n = []  # a_n[] são as colunas de N
x = []
x_x_b = []  # solução_avaliada
x_x_b = np.multiply(np.linalg.inv(B), b)
if x_x_b >= 0:
    print("solução básica viável")
Lambda = []  # vetor multiplicador simplex

c = []  # vetor de custos
c_b = []  # vetor de coeficientes das variáveis básicas
c_n = []  # vetor de coeficientes das variáveis não básicas
# custos relativos não básicos
c_xapeu_n = c_n[:] - np.multiply(Lambda.T, a_n[:])
y = []  # direção do simplex
# Errado. quero pegar as colunas de N
y[:] = np.multiply(np.linalg.inv(B), N[:])
c_xapeu_k = []  # teste de otimalidade nas não básicas
min{c_n}
E_xapeu = []
E_xapeu[:] = x_x_b[:]/y[:]
# np.linalg.inv(B)

"""
