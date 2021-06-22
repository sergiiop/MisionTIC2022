matriz = [[5,4,3],[2,1,0],[8,9,10]]

for i in range(0,len(matriz)):
    lista = len(matriz[i])
    for j in range(0,lista):
        print(matriz[i][j], end = '\t')
    print('\n')
