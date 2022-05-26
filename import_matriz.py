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
# append
# lista_aux = np.arange(n)
c_t = np.arange((len(auxiliar_custos)-1)/2)
print("olha o tamanho do vetor: ",len(c_t))
print(auxiliar_custos)
for i in range(len(auxiliar_custos)-1):

    #print(i)
    if i % 2 == 0: # pegando só os indeces pares.
        #print(i)
        print(int(auxiliar_custos[i]))
        c_t[int(i/2)]=int(auxiliar_custos[i])
        #print("dividindo i por 2: ", i/2)

print("vetor de custos: ", c_t)

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
while(texto != None):
    print()
    texto = texto.split('\n')[0]
    print(texto)
    result = re.search(r',', texto)
    # print(result)
    if result != None:
        print("Restrições: ",b)
        variaveis = texto.split(',')
        print("Variação:")
        print(variaveis)
        exit()
    else:
        # texto = "5*x1+2*x2<=5"
        aux = re.findall(r'=|<=|>=', texto)
        print(aux)  # ['<=']
        restricao = texto.split(aux[0])
        print("Restrição: ", restricao)

        result = re.findall(r'.[.\w\d]*', restricao[0])
        print(result)  # ['5', '*x1', '+2', '*x2']
        linha = []
        for i in range(len(result)-1):

            #print(i)
            if i % 2 == 0: # pegando só os indeces pares.
                #print(i)
                linha.append(int(result[i]))
                print(linha)
                #print("dividindo i por 2: ", i/2)
        print("PROBLEMA A SER RESOLVIDO FACILMENTE: RESTRIÇÕES ESTÃO SENDO MONTADAS ERRONEAMENTE QUANDO AS PRIMEIRAS \n variaveis não estão na restrição.")
        if(len(linha)<len(c_t)):
            for i in range(len(c_t)-len(linha)):
                linha.append(0)
        A.append(linha)
        b.append(float(fractions.Fraction(restricao[1])))
        print("matriz A:")
        print(A)
        aux_index_b+=1
        print(float(fractions.Fraction(restricao[1])))  # 2
        
        print()
    texto = arq.readline()
print("OLá")
print(A)
