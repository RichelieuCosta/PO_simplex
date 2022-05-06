import numpy as np
from itertools import combinations

# 1) escrever modelo dual na tela - fácil, mas pendente
# 2) simplex  - quase ok
# 3) determinar valores da solução primal - quase ok
# 4) determinar valores da solução dual - acho que vai ser super tranquilo depois de terminar de checar o primal
# 5) determinar ranges do lado direito - checar slides de anand pra comparar com anotações da disciplna da graduação


def atualizeBN(A, I_b, I_n):
    B = []
    N = []
    print("cuidado agora!!!")
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
    print(np.matrix(N).getT().getT())
    return np.asarray(B), np.asarray(N)


def obter_particoes_iniciais(A, b):

    len(A)
    I_b = []
    I_n = []

    n = len(A[1])
    m = len(A)

    lista_aux = np.arange(n)  # inicia vetor pelo valor 0
    lista_aux += 1  # Para começar pelo valor 1

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
        # print("O x chapeu: ", x_x_b)
        if x_x_b.min() >= 0:
            print("Conjunto legal pra iniciar!!", i_b)
            print("O x chapeu que passou: ")
            print(x_x_b)
            for i_n in lista_aux:
                if i_b.count(i_n) == 0:
                    # print(i_n, " Não está está na partição básica")
                    I_n.append(i_n)
                else:
                    I_b.append(i_n)

            break
    return I_b, I_n


def obter_custos(I_b, I_n, c_t):
    c_b = []
    c_n = []
    # print("atenção, para tudo!!!") # Alarme falso

    for i in I_b:

        c_b.append(c_t[i-1])
    for i in I_n:
        c_n.append(c_t[i-1])
    # print(c_b)
    # print(c_n)
    return c_b, c_n


def obter_coluna(M, j):
    coluna = []
    for linha in M:
        coluna.append(linha[j])  # coluna.append(linha[j-1]) #errei feio aqui.
    print("função de obter coluna")
    print("Perdi a minha noite inteira por conta dessa porqueira")
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

    print("partições básicas:")
    print(I_b)
    print("partições não básicas:")
    print(I_n)

    B, N = atualizeBN(A, I_b, I_n)
    c_b, c_n = obter_custos(I_b, I_n, c_t)

    print("b:")

    print(np.matrix(b).getT())

    print("matriz Básica:")
    print(B)
    print("matriz não básica:")
    print(N)
    B_inv = np.linalg.inv(B)
    print("B_inv:")
    print(B_inv)

    x_x_b = []  # solução_avaliada
    x_x_b = B_inv.dot(np.matrix(b).getT())
    print("custos das variáves básicas: ", c_b)
    lambda_t = np.matrix(c_b).dot(B_inv)

    print("valor de lambda: ", lambda_t)
    print(N)
    c_xapeu_n = np.arange(len(I_n))
    for j in range(len(I_n)):
        # custos relativos não básicos
        print("c_n[", j, "]: ", c_n[j])
        print("Coluna ", j, " de N: ", obter_coluna(N, j))
        c_xapeu_n[j] = c_n[j] - lambda_t.dot(obter_coluna(N, j))
        # print("c chapeu J:", j, c_xapeu_n[j])

    print("c xapeu n", c_xapeu_n)

    y = np.arange(len(A))

    if c_xapeu_n.min() < 0:
        for k in range(len(I_n)):
            print("valor de k: ", k)
            if c_xapeu_n[k] < 0:
                print("a kaézima variável não básica vai entrar na base?")
                if c_xapeu_n.min() == c_xapeu_n[k]:
                    print(
                        "a kaézima variável não básica VAI entrar, que é a variável: ", I_n[k])
                    index_entrar = k
                    for k in range(len(I_n)):
                        y = B_inv.dot(obter_coluna(N, k))
                    print("y: ", y)
                    if y.any() <= 0:
                        print("não tem solução ótima finita!")
                        return [0, 0, 0], I_b, I_n, x_x_b
                    break

                else:
                    print("a kaézima variável não básica NÃO vai entrar")
            else:
                print("acho que deu certo!! será??")
    else:
        print("Solução ótima, acabou!")
        return c_xapeu_n, I_b, I_n, x_x_b

    print("não foi dessa vez. Próxima iteração!")
    x_b_l = np.arange(len(y))
    for i in range(len(y)):
        if y[i] != 0:
            x_b_l[i] = x_x_b[i]/y[i]

    # x_b_l = x_x_b[:]/y[:]
    print("xxbl: ", x_b_l)
    for l in range(len(I_b)):
        #print("checando o lanço para sair da fase 2")
        if x_b_l.min() == x_b_l[l] and y[l] != 0:
            print("A variável a sair da base será: ", I_b[l], "de index: ", l)
            index_sair = l

    aux_troca = I_b[index_sair]
    I_b[index_sair] = I_n[index_entrar]
    I_n[index_entrar] = aux_troca
    return c_xapeu_n, I_b, I_n, x_x_b


c_t = np.array([-2, -1, 0, 0, 0])
A = np.array([[1, 1, 1, 0, 0],
              [1, 0, 0, 1, 0],
              [0, 1, 0, 0, 1]])


b = np.array([4, 3, 7/2])


#I_b, I_n = obter_particoes_iniciais(A, b)

I_b = [3, 1, 5]
I_n = [4, 2]

x = 0
while(x == 0):
    c_xapeu_n, I_b, I_n, x_x_b = primal_simplex(A, b, c_t, I_b, I_n)
    if c_xapeu_n.min() >= 0:
        print("i_b: ", I_b)
        print("x_x_b: ", x_x_b)
        print("fim")
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
