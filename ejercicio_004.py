# 2X3
A = [[1,2,3],
    [4,5,6]]

# 3X2
B = [[-1,0],
    [0,1],
    [1,1]]

# 2X2 por que es el 2 de las filas de A y el 2 de las columnas de B
C = [[0,0],
     [0,0]]

for i in range(0,2): #Empezamos en la columna y fila 0 de la matriz A, y el número de filas es 2.
    for j in range(0,2): #Empezamos en la columna y fila 0 de la matriz B, y el número de columnas es 2.
        for k in range(0,3): #Empezamos en la columna y fila 0 de la matriz B, y el número de filas es 3.
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

for row in C:
    print(row)

# https://www.youtube.com/watch?v=JlbqBc02JdU