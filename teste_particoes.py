import numpy as np
from itertools import combinations


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
    I_b = []
    I_n = []

    n = len(A[1])
    m = len(A)

    lista_aux = np.arange(n)
    lista_aux += 1

    comb = combinations(lista_aux, m)

    for i_b in comb:
        B = []
        for linhaA in A:
            linhaB = []
            for j in i_b:
                # print(j)
                linhaB.append(linhaA[j-1])
                # print(linhaB)
            B.append(linhaB)

        Binv = np.linalg.inv(np.matrix(B))
        x_x_b = []  # solução_avaliada
        x_x_b = Binv.dot(np.matrix(b).getT())
        print("olhaquii o x chapeu: ", x_x_b)
        if x_x_b.min() >= 0:
            print("Conjunto legal!!", i_b)
            for i_n in lista_aux:
                if i_b.count(i_n) == 0:
                    print(i_n, " Não está está na partição básica")
                    I_n.append(i_n)
                else:
                    I_b.append(i_n)

            break
    return I_b, I_n

    # Binv = np.linalg.inv(np.matrix(B))

    # print(Binv)
    # x_x_b = []  # solução_avaliada
    # x_x_b = Binv.dot(np.matrix(b).getT())

    return I_b, I_n


def obter_custos(I_b, I_n, c_t):
    c_b = []
    c_n = []

    for i in I_b:
        c_b.append(c_t[i-1])
    for i in I_n:
        c_n.append(c_t[i-1])

    return c_b, c_n


def obter_coluna(M, j):
    coluna = []
    for linha in M:
        coluna.append(linha[j-1])
    # print("função de obter coluna")
    # print(coluna)
    # print(np.matrix(coluna).getT())

    return np.matrix(coluna).getT()


def primal_simplex(A, b, c_t, I_b, I_n):

    index_entrar = 0
    index_sair = 0

    n = len(A[1])
    m = len(A)
    # m # numero de equações
    # n # número de variáveis

    print("partições básicas:", I_b)
    print("partições não básicas:", I_n)

    B, N = atualizeBN(A, I_b, I_n)
    c_b, c_n = obter_custos(I_b, I_n, c_t)

    print("Saiu da função de atualização de BN")

    print("b:", np.matrix(b).getT())
    print("matriz Básica:")
    print(B)

    print("matriz não básica")
    print(N)
    B_inv = np.linalg.inv(B)
    print("B_inv")
    print(B_inv)
    x_x_b = []  # solução_avaliada
    x_x_b = B_inv.dot(np.matrix(b).getT())

    lambda_t = np.matrix(c_b).dot(B_inv)

    print("valor de lambda: ", lambda_t)

    c_xapeu_n = np.arange(len(I_n))
    for j in range(len(I_n)):
        # custos relativos não básicos
        # c_xapeu_n[j] = c_n[j] - np.multiply(lambda_t, obter_coluna(N, j))
        c_xapeu_n[j] = c_n[j] - lambda_t.dot(obter_coluna(N, j))
        print("c chapeu J:", j, c_xapeu_n[j])

    print(c_xapeu_n)
    y = np.arange(len(A))
    if c_xapeu_n.min() < 0:
        for k in range(len(I_n)):
            print("valor de k: ", k)
            if c_xapeu_n[k] < 0:
                print("a kaézima variável não básica vai entrar na base?")
                if c_xapeu_n.min() == c_xapeu_n[k]:
                    print("a kaézima variável não básica VAI entrar")
                    index_entrar = k
                    for k in range(len(I_n)):
                        y = B_inv.dot(obter_coluna(N, k))
                    print("y: ", y)
                    break

                else:
                    print("a kaézima variável não básica NÃO vai entrar")
            else:
                print("acho que deu certo!!")
    else:
        print("Solução ótima, acabou!")
        return c_xapeu_n, I_b, I_n

    print("não foi dessa vez")
    x_b_l = x_x_b[:]/y[:]
    print("xxbl: ", x_b_l)
    for l in range(len(I_b)):
        if x_b_l.min() == x_b_l[l]:
            print("A variável a sair da base será: ", I_n[l], "de index: ", l)
            index_sair = l

    aux_troca = I_b[index_sair]
    I_b[index_sair] = I_n[index_entrar]
    I_n[index_entrar] = aux_troca
    return c_xapeu_n, I_b, I_n


print("oxente 1 ")
c_t = np.array([2, 4, 1, 0, 0])
A = np.array([[1, 1, 1, 0, 0],
              [1, -1, 0, 1, 0],
              [3, 1, 0, 0, -1]])


b = np.array([6, 4, 3])


print("oxente 2 ")
I_b, I_n = obter_particoes_iniciais(A, b)


x = 0
while(x == 0):
    print("eeei", I_b)
    c_xapeu_n, I_b, I_n = primal_simplex(A, b, c_t, I_b, I_n)
    if c_xapeu_n.min() >= 0:
        print("acaboooooou")
        x = 1
    else:
        print("Ainda não acabou")

    # y=np.arange(len(I_b))
    # for k in range(len(I_n)):
    #    # custos relativos não básicos
    #    #c_xapeu_n[j] = c_n[j] - np.multiply(lambda_t, obter_coluna(N, j))
    #    c_xapeu_n[j] = c_n[j] - B_inv.dot(obter_coluna(N, j))
    #    print("c chapeu J:", j, c_xapeu_n[j])
    #    y[:] = np.multiply(np.linalg.inv(B),N[:])


# if x_x_b.min() >= 0:
#    print("Conjunto legal!!")
# print("m:", m)
# print("n:", n)
# print(x_x_b)


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

# resolvendo sistema de equações lineares:
# Solve the system of equations x0 + 2 * x1 = 1 and 3 * x0 + 5 * x1 = 2:
# a = np.array([[1, 2], [3, 5]])
# b = np.array([1, 2])
# x = np.linalg.solve(a, b)
# x

N = np.zeros( (1,1) ) # matrix_NãoBásica
a_n = np.arange(1) # a_n[] são as colunas de N
x = np.arange(1)

if x_x_b >= 0:
    print("solução básica viável")
Lambda = np.arange(1) # vetor multiplicador simplex
lambda_t = c_b.getT().dot(B_inv)
c = np.arange(1) # vetor de custos
c_b = np.arange(1)  # vetor de coeficientes das variáveis básicas
c_n = np.arange(1) # vetor de coeficientes das variáveis não básicas
# custos relativos não básicos
c_xapeu_n = c_n[:] - np.multiply(Lambda.T,a_n[:])
y = np.arange(1) # direção do simplex
y[:] = np.multiply(np.linalg.inv(B),N[:]) # Errado. quero pegar as colunas de N
c_xapeu_k = np.arange(1) # teste de otimalidade nas não básicas
 min{c_n}
E_xapeu = np.arange(1)
E_xapeu[:] = x_x_b[:]/y[:]
# np.linalg.inv(B)

"""
