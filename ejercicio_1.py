import numpy as np
matriz_a = np.random.randint(1, 11, (10, 10))
print(matriz_a)
vector_r = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
        if matriz_a[i][j] == 1:
            vector_r[0] += 1
        if matriz_a[i][j] == 2:
            vector_r[1] += 1
        if matriz_a[i][j] == 3:
            vector_r[1] += 1
        if matriz_a[i][j] == 4:
            vector_r[2] += 1
        if matriz_a[i][j] == 5:
            vector_r[4] += 1
        if matriz_a[i][j] == 6:
            vector_r[5] += 1
        if matriz_a[i][j] == 7:
            vector_r[6] += 1
        if matriz_a[i][j] == 8:
            vector_r[7] += 1
        if matriz_a[i][j] == 9:
            vector_r[8] += 1
        if matriz_a[i][j] == 10:
            vector_r[9] += 1
print(vector_r)
print(np.sum(vector_r))
