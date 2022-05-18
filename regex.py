import re

texto = "min f(x[])=-2*x1-2*x2"

aux = texto.split('=')
print(aux[0], '=', aux[1])

# result = re.findall(r'.[.\w\d]*', '5*x1+2*x2')
# print(int(result[2])) #2
# print(result) # ['5', '*x1', '+2', '*x2']

texto = "sujeito a:"
if texto == "sujeito a:":
    print("sujeito a:")

texto2 = "5*x1+2*x2<=5"
result = re.findall(r'=|<=|>=', texto2)
print(result)  # ['<=']
restricao = texto2.split(result[0])
print(restricao)

result = re.findall(r'.[.\w\d]*', restricao[0])
print(int(result[2]))  # 2
print(result)  # ['5', '*x1', '+2', '*x2']

texto = 'x2>=0,x1>=0,x3>=0'
result = re.search(r',', texto)
# print(result)
if result != None:
    variaveis = texto.split(',')
    print("olaaa")
    print(variaveis)
