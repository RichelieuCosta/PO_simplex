
# $$$$$$$$$$$$$$$$$$%%%%%%%%%%%%%%%%%%

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
# A = np.array([[4/5, 2/5, 0],
#             [0, 3/5, 9/9]])
#b = np.array([108, 120])

c_t = np.array([1, 1, 0, 0])
A = np.array([[2, 1, -1, 0],
             [1, 3, 0, -1]])
b = np.array([4, 3])

# Entradas precisam ser de minimizar e com range das variáves >=0

# 1
min f(x[]) = 1*x1+1*x2
sujeito a:
2*x1+1*x2 <= 4
1*x1+3*x2 <= 3
x1 >= 0, x2 >= 0

# 2
min f(x[]) = 1*x1+2*x2
sujeito a:
−2*x1+1*x2 <= 3
3*x1+4*x2 <= 5
1*x1−1*x2 <= 2
x1 >= 0, x2 >= 0

# 3  #### a tratar entrada
# max f (x[]) = −min −f(x[]),
max f(x[]) = 1*x1+2*x2
sujeito a:
−2*x1+1*x2+1*x3 >= 3
3*x1+4*x2 <= 5
x1 >= 0, x2 livre, x3 <= 0

# 4
min f(x[]) = 2*x1+3*x2+2*x3+1*x4
sujeito a:
−1*x1+1*x2−2*x3−1*x4 = 2
2*x1+1*x2−3*x3 = 1
x1 >= 0, x2 >= 0, x3 >= 0, x4 >= 0

# 5
min f(x[]) = 3*x1+5*x3+4*x4
sujeito a:
1*x1−1*x2+2*x3−3*x4 = 1
2*x1+1*x2−3*x3+4*x4 = 3
x1 >= 0, x2 >= 0, x3 >= 0, x4 >= 0
