import numpy as np
matriz_a = np.random.randint(1, 11, (10, 10))
print(matriz_a)
r = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(len(matriz_a)):
    for j in range(len(matriz_a[i])):
