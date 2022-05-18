from ctypes import c_bool
from imp import is_builtin
import numpy as np
arq = open('arquivo.txt', 'r')  # abre o arquivo
texto = []  # declaro um vetor
matriz = []  # declaro um segundo vetor
texto = arq.readline()  # quebra as linhas do arquivo em vetores
print("vetor texto -> ", texto)  # aqui eu mostro
"""
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
