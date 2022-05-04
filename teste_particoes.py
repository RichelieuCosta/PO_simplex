import numpy as np

def obter_particoes(A,b):
    len(A)
    I_b=np.zeros((len(A)), dtype=int)
    I_n=np.zeros((len(A[1])-len(A)), dtype=int)


    
    return I_b, I_n

A= [[1, 1, 1, 0, 0],
    [1, -1, 0, 1, 0],
    [3, 1, 0, 0, -1]]
    
for l in A:
    print(l)

b= [6, 4, 3]

I_b = [] #indice das variáveis que estão na partição básica
I_n = [] #indice das variáveis que estão na partição não básica
# A_inv = []
print("ola")
I_b, I_n=obter_particoes(A, b)

print(I_b)
print(I_n)

