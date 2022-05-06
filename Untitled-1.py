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
    print("Solução ótima!")

x_b_l = x_x_b[:]/y[:]
print("xxbl: ", x_b_l)
for l in range(len(I_b)):
    if x_b_l.min() == x_b_l[l]:
        print("A variável a sair da base será: ", I_n[l], "de index: ", l)
        index_sair = l


aux_troca = I_b[index_sair]
I_b[index_sair] = I_n[index_entrar]
I_n[index_entrar] = aux_troca
