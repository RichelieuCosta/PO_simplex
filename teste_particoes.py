import numpy as np
from itertools import combinations

# 1) escrever modelo dual na tela - OK
# 2) simplex  -  ok
# 3) determinar valores da solução primal -  ok
# 4) determinar valores da solução dual - acho que vai ser super tranquilo depois de terminar de checar o primal
# 5) determinar ranges do lado direito - checar slides de anand pra comparar com anotações da disciplna da graduação


def atualizeBN(A, I_b, I_n):
    B = []
    N = []
    # print("cuidado agora!!!")
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
    # print(np.matrix(N).getT().getT())
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
        print("O x chapeu: ", x_x_b)
        aux_menor = x_x_b[0]
        # if x_x_b.min() >= 0:
        for x_x_b_i in x_x_b:
            if x_x_b_i < aux_menor:
                aux_menor = x_x_b_i
        if aux_menor >= 0:
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
    # print("função de obter coluna")
    # print("Perdi a minha noite inteira por conta dessa porqueira")
    # print(coluna)
    # print(np.matrix(coluna).getT())

    return np.matrix(coluna).getT()


def escrever_problema_primal(A, c_t, b):
    print("PROBLEMA PRIMAL***************")
    print("vetor de custos das variáveis:")
    print(c_t)

    print("matriz de coeficientes:")
    print(np.matrix(A))

    print("vetor das restrições: IGUAL A")
    print(np.matrix(b).getT())


def escrever_problema_dual(A, b, c_t):
    print("PROBLEMA DUAL***************")
    print("vetor de custos das variáveis:")
    print(c_t)

    print("matriz de coeficientes:")
    print(np.matrix(A).getT())

    print("vetor das restrições: MENOR IGUAL A")
    print(np.matrix(b).getT())


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
    print("custos das variáves não básicas: ", c_n)
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
                    aux_count = 0
                    for y_i in y:
                        if y_i <= 0:
                            y_i += 1
                    if aux_count == len(y):
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
    print("x_x_b: ", x_x_b)
    epsilon_xapeu = np.arange(len(y))
    for i in range(len(y)):
        if y[i] > 0:
            epsilon_xapeu[i] = x_x_b[i]/y[i]

    aux_MIN_epsilon_xapeu = 0
    index_sair = 0
    for i in range(len(y)):
        if y[i] > 0:
            # por falta de prática com python, escolhi essa forma de pegar o menor valor de epsilon_xapeu
            aux_MIN_epsilon_xapeu = epsilon_xapeu[i]
            index_sair = i

    for i in range(len(y)):
        if y[i] > 0 and epsilon_xapeu[i] < aux_MIN_epsilon_xapeu:
            aux_MIN_epsilon_xapeu = epsilon_xapeu[i]
            index_sair = i
    # epsilon_xapeu = x_x_b[:]/y[:]
    print("   'epsilon_xapeu': ", epsilon_xapeu)
    print("epsilon_xapeu menor: ", epsilon_xapeu[index_sair])
    print("A variável a sair da base será: ",
          I_b[index_sair], "de index: ", index_sair)

    aux_troca = I_b[index_sair]
    I_b[index_sair] = I_n[index_entrar]
    I_n[index_entrar] = aux_troca
    return c_xapeu_n, I_b, I_n, x_x_b


def dual_simplex(A, b, c_t):  # , I_b, I_n):

    I_b, I_n = obter_particoes_iniciais(A, b)

    index_entrar = 0
    index_sair = 0

    # número de variáveis Primal. O numero de restricoes duais ́e igual ao n ́umero de variáveis X do primal
    n = len(A)
    m = len(A[1])  # numero de equações do primal
    # m
    # n

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
    print("custos das variáves não básicas: ", c_n)
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
                    aux_count = 0
                    for y_i in y:
                        if y_i <= 0:
                            y_i += 1
                    if aux_count == len(y):
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
    print("x_x_b: ", x_x_b)
    epsilon_xapeu = np.arange(len(y))
    for i in range(len(y)):
        if y[i] > 0:
            epsilon_xapeu[i] = x_x_b[i]/y[i]

    aux_MIN_epsilon_xapeu = 0
    index_sair = 0
    for i in range(len(y)):
        if y[i] > 0:
            # por falta de prática com python, escolhi essa forma de pegar o menor valor de epsilon_xapeu
            aux_MIN_epsilon_xapeu = epsilon_xapeu[i]
            index_sair = i

    for i in range(len(y)):
        if y[i] > 0 and epsilon_xapeu[i] < aux_MIN_epsilon_xapeu:
            aux_MIN_epsilon_xapeu = epsilon_xapeu[i]
            index_sair = i
    # epsilon_xapeu = x_x_b[:]/y[:]
    print("   'epsilon_xapeu': ", epsilon_xapeu)
    print("epsilon_xapeu menor: ", epsilon_xapeu[index_sair])
    print("A variável a sair da base será: ",
          I_b[index_sair], "de index: ", index_sair)

    aux_troca = I_b[index_sair]
    I_b[index_sair] = I_n[index_entrar]
    I_n[index_entrar] = aux_troca
    return c_xapeu_n, I_b, I_n, x_x_b


def resolver_por_primal(A, b, c_t):
    I_b, I_n = obter_particoes_iniciais(A, b)

    # I_b = [3, 1, 5]
    # I_n = [4, 2]

    c_xapeu_n = []
    x_x_b = []

    x = 0
    while(x == 0):
        c_xapeu_n, I_b, I_n, x_x_b = primal_simplex(A, b, c_t, I_b, I_n)
        if c_xapeu_n.min() >= 0:
            print("i_b: ", I_b)
            print("i_n: ", I_n)
            print("x_x_b: ")
            print(x_x_b)
            print("fim")
            x = 1
        else:
            print("Ainda não acabou")

    # vetor de variáveis do tamanho da quantidade de variáveis
    x_final = np.arange(len(A[1]), dtype=float)

    # print(x_final) # preenchido com lixo, por falta de habilidades simples em python.
    for i in range(len(I_n)):
        x_final[I_n[i]-1] = 0
    # print(x_final)
    for i in range(len(I_b)):
        x_final[I_b[i]-1] = x_x_b[i].copy()
    # print(x_final)

    print("vetor X na sequencia original: ", x_final)
    print("vetor de custos: ", c_t)
    print("valor da solução ótima: ", x_final.dot(c_t))
    return x_final


def resolver_por_dual(A, b, c_t):
    I_b, I_n = obter_particoes_iniciais(np.matrix(A).getT(), b)

    dual_simplex(np.matrix(A).getT(), c_t, b, I_b, I_n)

    return


# c_t = np.array([-2, -1, 0, 0, 0])
# A = np.array([[1, 1, 1, 0, 0],
#              [1, 0, 0, 1, 0],
#              [0, 1, 0, 0, 1]])
# b = np.array([4, 3, 7/2])


#c_t = np.array([-3, -5, 0, 0, 0])
# A = np.array([[1, 0, 1, 0, 0],
#             [0, 1, 0, 1, 0],
#             [3, 2, 0, 0, 1]])
#b = np.array([4, 6, 18])

c_t = np.array([1, 1, 1])
A = np.array([[4/5, 2/5, 0],
             [0, 3/5, 9/9]])
b = np.array([108, 120])

#escrever_problema_primal(A, c_t, b)
escrever_problema_dual(A, c_t, b)

#print("primal: ", resolver_por_primal(A, b, c_t))

# print("Dual: ", resolver_por_dual(np.matrix(A).getT(), c_t, b,))
