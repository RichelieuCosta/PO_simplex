from ctypes import c_bool
from imp import is_builtin
import re
import numpy as np
import fractions

arq = open('arquivo.txt', 'r')  # abre o arquivo
texto = []  # declaro um vetor
matriz = []  # declaro um segundo vetor
texto = arq.readline()  # quebra as linhas do arquivo em vetores
print("vetor texto -> ", texto)  # aqui eu mostro

aux = texto.split('=')
print(aux[0], '=', aux[1])

auxiliar_custos= re.findall(r'.[.\w\d]*', aux[1])
print("olha a auxiliar custos: ",auxiliar_custos)
# append
# lista_aux = np.arange(n)
v_v = []
num_var = int((len(auxiliar_custos))/2) # SUBTRAIR 1 AQUI O AUXILIAR CUSTOS ?
print("Olha a quantidade de variaveis: ", num_var)
c_t = [] #np.arange((len(auxiliar_custos)-1)/2)
qtd_var_folgas = 0
#print("olha o tamanho dos vetores: ",c_t, len(v_v) )
print(auxiliar_custos)
for i in range(len(auxiliar_custos)): # SUBTRAIR 1 AQUI O AUXILIAR CUSTOS?

    #print(i)
    if i % 2 == 0: # pegando só os indeces pares.
        #print(i)
        print(int(auxiliar_custos[i]))
        c_t.append(int(auxiliar_custos[i]))#[int(i/2)]
        #print("dividindo i por 2: ", i/2)
    else:
        #print("Olha o valor no else", int((i-1)/2))
        v_v.append(auxiliar_custos[i])

print("vetor de custos: ", c_t)
#c_t=np.asarray(c_t)
print(c_t)
print("vetor de variáveis: ", v_v)

texto = arq.readline()
print(texto)
if texto == "sujeito a:\n":
    print("sujeito a:")
else:
    print("FOrmato inválido")
    exit()

texto = arq.readline()
A = []
b = []
aux_index_b = 0
igualdades_restricoes = []
while(texto != None):
    print()
    texto = texto.split('\n')[0]
    print(texto)
    result = re.search(r',', texto)
    # print(result)
    if result != None:
        print("Restrições: ",b)
        print(np.asarray(b))
        variaveis = texto.split(',')
        print("Variação:")
        print(variaveis)
        break
    else:
        # texto = "5*x1+2*x2<=5"
        aux = re.findall(r'=|<=|>=', texto)
        igualdades_restricoes.append(aux)
        print(aux)  # ['<=']
        if aux[0] == '=':
            print("entrei pq a restrição é de igualdade")
        else:
            qtd_var_folgas+=1
            #print("aumentar tamanho de c_t")
            c_t.append(0)

        restricao = texto.split(aux[0])
        print("Restrição: ", restricao)

        result = re.findall(r'.[.\w\d]*', restricao[0])
        print(result)  # ['5', '*x1', '+2', '*x2']
        linha = []
        i=1
        print("olha o meu print aleatório: ", (len(result)-1))
        while (i<=(len(result))):
        ##for i in range(len(result)-1):
            print("Mostrando variação do indice i ", i)
            # i += 1
            # inicio do pensamento atual

            for j in range(int((i-1)/2), (len(v_v)), 1):
                print("result[i] :", result[i], "\n v_v[j]:", v_v[j])
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
        print("matriz A:")
        print(A)
        print(np.asarray(A))
        aux_index_b+=1
        print(float(fractions.Fraction(restricao[1])))  # 2
        
        print()
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
print(np.asarray(A))

