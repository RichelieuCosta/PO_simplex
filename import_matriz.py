from ctypes import c_bool
from imp import is_builtin
import numpy as np
arq = open('arquivo.txt', 'r')  #abre o arquivo
texto = []  #declaro um vetor
matriz = [] #declaro um segundo vetor
texto = arq.readlines() #quebra as linhas do arquivo em vetores 
print("vetor texto -> ",texto) #aqui eu mostro
print("")

for i in range(len(texto)):          #esse for percorre a posições dp vetor texto
    matriz.append(np.array(texto[i].split()))  #aqui eu quebro nos espasos das palavras

print("vetor matriz -> ",matriz) #mostra o vertor com um conjunto de vetores
print("")

for i in range(len(texto)):          #mostra quedrando em linhas
    print(matriz[i])  


arq.close() #comando para fechar o arquivo


# variavéis que precisarei: 

A = []
A_inv = []

B = []
print(B.T)
b = []
# m== numero de equações
# n== número de variáveis
#resolvendo sistema de equações lineares:
#Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2:
#a = np.array([[1, 2], [3, 5]])
#b = np.array([1, 2])
#x = np.linalg.solve(a, b)
#x

N = []
a_n = [] # a_n[] são as colunas de N
x = []
x_x_b = []
x_x_b = np.multiply(np.linalg.inv(B),b)
if x_x_b >= 0:
    print("solução básica viável")
Lambda = []
I_b = []
I_n = []
c = []
c_b = []
c_n = []
c_xapeu_n = c_n - Lambda.T*a_n
y = 0
c_xapeu_k = min{c_n}
E_xapeu = min{x_x_b[]/y[]}
np.linalg.inv(B)
