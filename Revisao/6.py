def soma_diagonal_principal(matriz):
    soma = 0
    for i in range(len(matriz)):
        soma += matriz[i][i]
    return soma

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(soma_diagonal_principal(matriz))

# reposta: A, escolhi a alternativa B pois retorna uma matriz mas não a diagonal principal.






