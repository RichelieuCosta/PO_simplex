import numpy as np
from itertools import combinations
from ctypes import c_bool
from imp import is_builtin
import re
import fractions
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Matrix, symbols

# 1) escrever modelo dual na tela - OK
# 2) simplex  -  ok
# 3) determinar valores da solução primal -  ok
# 3.1) determinar valores da solução dual a partir da primal - ok
# 4) determinar valores da solução dual - ok
#  atualização de nomes das variaveis dual e conclusão. - ok
# 5) determinar ranges do lado direito - OK.
## O que dá pra fazer:
#1. Variações nas quantidades de recursos; - OK
#2. Variações nos coeficientes da função objetivo; - pode ser feito
#3. Variações nos coeficientes das atividades;- pode ser feito
#4. Acréscimo de uma nova restrições.- pode ser feito
#5. Acréscimo de uma nova variável.- pode ser feito


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
    print("OBTENDO PARTIÇÔES iniciais")
    # len(A)
    I_b = []
    I_n = []
    print("Olha quem é A:")
    print(A)
    #print()
    #print(len(A[:,1]))
    #print(len(A[1,:]))
    #print(len(A[1]))
    #print(A[0][0])
    #print(A[1][0])
    n = len(A[0])
    m = len(A)
    print(n, m)
    lista_aux = np.arange(n)  # inicia vetor pelo valor 0
    lista_aux += 1  # Para começar pelo valor 1
    print("lista_aux")
    print(lista_aux)

    comb = combinations(lista_aux, m)
    
    for i_b in comb:
        #print(i_b)
        B = []
        for linhaA in A:
            linhaB = []
            for j in i_b:
                # print(j)
                linhaB.append(linhaA[j-1])
                print(linhaB)
            B.append(linhaB)

        Binv = np.linalg.inv(np.matrix(B))
        x_x_b = []  # solução_avaliada
        print(Binv)
        print(b)
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



def dual_simplex(A, b, c_t , I_b, I_n):

    #I_b, I_n = obter_particoes_iniciais(A, b)

    index_entrar = 0
    index_sair = 0

    # número de variáveis Primal. O numero de restricoes duais ́e igual ao numero de variáveis X do primal
    n = len(A)
    m = len(A[1])  # numero de equações do primal que é igual ao número de variaveis do dual
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
    B_t = np.matrix(B).getT()
    B_inv = np.linalg.inv(B)
    print("B_inv:")
    print(B_inv)

    print("custos das variáves básicas: ", c_b)
    print("custos das variáves não básicas: ", c_n)

    # Passo 1

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

    # Passo 2:

    # Passo 2.1:
    
    x_x_b = []  # solução_avaliada
    x_x_b = B_inv.dot(np.matrix(b).getT())

    # Passo 2.2:

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

    eta = np.arange(len(I_n))
    e_vetor_canonico = np.arange(len(I_n))
    if aux_menor < 0:
        # Passo 3
        for l in range(len(I_n)):
            print("valor de l: ", l)
            for l2 in range(len(I_n)):
                if l == l2:
                    e_vetor_canonico[l2] = 1
                else:
                    e_vetor_canonico[l2] = 0
            eta[l]=(-1)*(np.matrix(np.linalg.inv(B)).getT().dot(e_vetor_canonico))

        # Passo 4
        denominador_sigma = np.arange(len(I_n))
        for l in range(len(I_n)):
            denominador_sigma[l] = eta[l].dot(obter_coluna(N, j))
            if denominador_sigma[l] <= 0:
                print("problema primal inviável. Error!!!")
                return "error"

        sigma_analise = np.arange(len(I_n))
        sigma_analise = c_xapeu_n[:]/denominador_sigma[:]

        aux_MIN_sigma_xapeu = sigma_analise[0]
        index_entrar = 0
        for i in range(len(sigma_analise)):
            if sigma_analise[i] < aux_MIN_sigma_xapeu:
                aux_MIN_sigma_xapeu = sigma_analise[i]
                index_entrar = i

        print("   'epsilon_xapeu': ", epsilon_xapeu)
        print("epsilon_xapeu menor: ", epsilon_xapeu[index_sair])
        print("A variável a sair da base será: ",
            I_b[index_sair], "de index: ", index_sair)

        aux_troca = I_b[index_sair]
        I_b[index_sair] = I_n[index_entrar]
        I_n[index_entrar] = aux_troca
        return c_xapeu_n, I_b, I_n, x_x_b

            


    else:
        print("Solução ótima, acabou!")
        return c_xapeu_n, I_b, I_n, x_x_b

def obter_solucao_dual_dada_primal(B,c_b): # I_b, c_t

    #B_inv.dot(np.matrix(b).getT())
    B_inv_t = np.matrix(np.linalg.inv(B)).getT()
    lambda_xapeu = B_inv_t.dot(np.matrix(c_b).getT())
    print("lambda xapeu (solução do dual):")
    print(lambda_xapeu)
    #Aula 12 - dual 

    return lambda_xapeu

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

    B, N = atualizeBN(A, I_b, I_n)
    
    c_b, c_n = obter_custos(I_b, I_n, c_t)
    obter_solucao_dual_dada_primal(B,c_b)

    return B, x_final


def resolver_por_dual(A, b, c_t):
    print(A)
    print("olha a quantidade de colunas")
    print(len(A[0]))
    A_tansposta= A.transpose()
    print(A_tansposta)
    I_b, I_n = obter_particoes_iniciais(A_tansposta, b)

    

    c_xapeu_n = []
    x_x_b = []

    x = 0
    while(x == 0):
        c_xapeu_n, I_b, I_n, x_x_b = dual_simplex(A_tansposta, c_t, b , I_b, I_n)
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

def analise_variacao_qtd_recursos(B, b):
    
    z = symbols('Z', extended_real=True)
    Binv = Matrix(np.asarray(np.linalg.inv(np.matrix(B))))
    tupas_variacoes = []
    for i in range(len(b)):
            
        b_2=Matrix(b)
        b_2[i]+=z
        equa = Binv*b_2
        inequacao =[]
        for linha in equa:
            inequacao.append((linha,">"))
        inequacao2 = []
        inequacao2.append(inequacao)
        #print(inequacao2)
        result = reduce_rational_inequalities(inequacao2, z)
        print("Uma variação admissível no recurso", i, " do problema primal é somar um valor Z, desde que:", result)
       
        tupas_variacoes.append(result)

    return tupas_variacoes

def carregar_de_arquivo(caminho):

    arq = open(caminho, 'r')  # abre o arquivo
    texto = []  # declaro um vetor
    matriz = []  # declaro um segundo vetor
    texto = arq.readline()  # quebra as linhas do arquivo em vetores
    # print("vetor texto -> ", texto)  # aqui eu mostro

    aux = texto.split('=')
    print()
    print(aux[0], '=', aux[1])

    auxiliar_custos= re.findall(r'.[.\w\d]*', aux[1])
    # print("olha a auxiliar custos: ",auxiliar_custos)
    # append
    # lista_aux = np.arange(n)
    v_v = []
    num_var = int((len(auxiliar_custos))/2) # SUBTRAIR 1 AQUI O AUXILIAR CUSTOS ?
    # print("Olha a quantidade de variaveis: ", num_var)
    c_t = [] #np.arange((len(auxiliar_custos)-1)/2)
    qtd_var_folgas = 0
    # print("olha o tamanho dos vetores: ",c_t, len(v_v) )
    # print(auxiliar_custos)
    for i in range(len(auxiliar_custos)): # SUBTRAIR 1 AQUI O AUXILIAR CUSTOS?

        #print(i)
        if i % 2 == 0: # pegando só os indeces pares.
            #print(i)
            # print(int(auxiliar_custos[i]))
            c_t.append(int(auxiliar_custos[i]))#[int(i/2)]
            #print("dividindo i por 2: ", i/2)
        else:
            #print("Olha o valor no else", int((i-1)/2))
            v_v.append(auxiliar_custos[i])

    #print("vetor de custos: ", c_t)
    #c_t=np.asarray(c_t)
    #print(c_t)
    #print("vetor de variáveis: ", v_v)

    texto = arq.readline()
    print(texto)
    if texto == "sujeito a:\n":
        print()
        #print("sujeito a:")
    else:
        print("FOrmato inválido")
        exit()

    texto = arq.readline()
    A = []
    b = []
    aux_index_b = 0
    igualdades_restricoes = []
    while(texto != None):
       # print()
        texto = texto.split('\n')[0]
        print(texto)
        result = re.search(r',', texto)
        # print(result)
        if result != None:
            #print("Restrições: ",b)
            #print(np.asarray(b))
            variaveis = texto.split(',')
            #print("Variação:")
            #print(variaveis)
            break
        else:
            # texto = "5*x1+2*x2<=5"
            aux = re.findall(r'=|<=|>=', texto)
            igualdades_restricoes.append(aux)
            #print(aux)  # ['<=']
            if aux[0] == '=':
                print()
                #print("entrei pq a restrição é de igualdade")
            else:
                qtd_var_folgas+=1
                #print("aumentar tamanho de c_t")
                c_t.append(0)

            restricao = texto.split(aux[0])
            #print("Restrição: ", restricao)

            result = re.findall(r'.[.\w\d]*', restricao[0])
            #print(result)  # ['5', '*x1', '+2', '*x2']
            linha = []
            i=1
            #print("olha o meu print aleatório: ", (len(result)-1))
            while (i<=(len(result))):
            ##for i in range(len(result)-1):
                #print("Mostrando variação do indice i ", i)
                # i += 1
                # inicio do pensamento atual

                for j in range(int((i-1)/2), (len(v_v)), 1):
                    #print("result[i] :", result[i], "\n v_v[j]:", v_v[j])
                    if result[i]==v_v[j]:
                        linha.append(int(result[i-1]))
                        break
                    else:
                        linha.append(0)
                i +=2

                # fim do pensamento atual
                
            if(len(linha)<(num_var)):
                for i in range(num_var-len(linha)):
                    linha.append(0)
            A.append(linha)
            b.append(float(fractions.Fraction(restricao[1])))
            #print("matriz A:")
            #print(A)
            #print(np.asarray(A))
            aux_index_b+=1
            #print(float(fractions.Fraction(restricao[1])))  # 2
            
            #print()
        texto = arq.readline()
    print("vamos prosseguir")
    # igualdades_restricoes
    colunas_adicionadas = 0
    for i, linha in enumerate(A):

        #print(linha, igualdades_restricoes[i])
        for aux in range(colunas_adicionadas):
            #print("to em colunas adicionadas")
            linha.append(0)

        if(len(linha)<(len(c_t)+qtd_var_folgas)):
            #print("to deixando na forma padrão", igualdades_restricoes[i])
            #print(igualdades_restricoes[i][0]=='<=')
            if igualdades_restricoes[i][0]=='<=':
                #print("adicionando 1")
                linha.append(1)
                colunas_adicionadas+=1
            elif igualdades_restricoes[i][0]=='>=':
                #print("adicionando -1")
                linha.append(-1)
                colunas_adicionadas+=1
            else:
                linha.append(0)
                colunas_adicionadas+=1
            for aux in range(qtd_var_folgas-colunas_adicionadas):
                #print("resolvendo o lado direito")
                linha.append(0)
            #print("Terminei uma linha", linha)
    #print(np.asarray(A))



    return A, b, c_t, igualdades_restricoes

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

#c_t = np.array([1, 1, 1])
#A = np.array([[4/5, 2/5, 0],
#             [0, 3/5, 9/9]])
#b = np.array([108, 120])

#c_t = np.array([1, 1, 0, 0])
#A = np.array([[2, 1, -1, 0],
#             [1, 3, 0, -1]])
#b = np.array([4, 3])
A, b, c_t, igualdades_restricoes = carregar_de_arquivo('arquivo.txt')
# Atenção, o parse não aceita frações. para corrigir isso, 
# modificar a expressão regular que pega os coeficientes

#print(c_t)
#print(np.asarray(A))
#print(np.matrix(b).getT())

escrever_problema_primal(A, c_t, b)
escrever_problema_dual(A, c_t, b)
B, solucao_otima = resolver_por_primal(A, b, c_t)
print("primal: ", solucao_otima)

analise_variacao_qtd_recursos(B, b)

#print("Dual: ", resolver_por_dual(A, c_t, b)) # A FORMA DE OBTER AS BASES INICIAIS NÃO FUNCIONA COMO É FEITO NO PRIMAL
