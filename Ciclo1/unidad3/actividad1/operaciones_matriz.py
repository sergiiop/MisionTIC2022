matriz = [[5, 4, 3], [2, 1, 0], [8, 9, 10]]
matriz2 = [[3, 4, 5], [0, 1, 2], [10, 9, 8]]
matriz3 = []
matriz4 = []
matriz5 = []

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz3.append(matriz[i][j] + matriz2[i][j])#matriz 3 es una lista que agrega los resultados

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz4.append(matriz[i][j] - matriz2[i][j])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz5.append(matriz[i][j] * 2)

print('Suma')
print(matriz3)
print('resta')
print(matriz4)
print('multipicacion')
print(matriz5)
