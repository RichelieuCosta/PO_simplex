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
print(auxiliar_custos)
for i in range(len(auxiliar_custos)-1):

    #print(i)
    if i % 2 == 0: # pegando só os indeces pares.
        #print(i)
        print(auxiliar_custos[i])
    

texto = arq.readline()
print(texto)
if texto == "sujeito a:\n":
    print("sujeito a:")
else:
    print("FOrmato inválido")
    exit()

texto = arq.readline()
while(texto != None):
    print()
    texto = texto.split('\n')[0]
    print(texto)
    result = re.search(r',', texto)
    # print(result)
    if result != None:
        variaveis = texto.split(',')
        print("Variação:")
        print(variaveis)
        exit()
    else:
        #texto = "5*x1+2*x2<=5"
        aux = re.findall(r'=|<=|>=', texto)
        print(aux)  # ['<=']
        restricao = texto.split(aux[0])
        print(restricao)

        result = re.findall(r'.[.\w\d]*', restricao[0])

        print(float(fractions.Fraction(restricao[1])))  # 2
        print(result)  # ['5', '*x1', '+2', '*x2']
        print()
    texto = arq.readline()
