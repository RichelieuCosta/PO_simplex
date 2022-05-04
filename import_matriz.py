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

N = []
a_n = [] # a_n[] são as colunas de N
x = []
x_x_b = []
x_x_b = np.multiply(np.linalg.inv(B),b)
Lambda = []
I_b = []
I_n = []
c_b = []
c_n = []
c_xapeu_n = c_n - Lambda.T*a_n
y = 0
c_xapeu_k = min{c_n}
E_xapeu = min{x_x_b[]/y[]}
np.linalg.inv(B)