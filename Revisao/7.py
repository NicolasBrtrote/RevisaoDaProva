#CODIGO A
lista = [x for x in range(5)]
print(lista)

#CODIGO B
lista = list(range(5))
print(lista)

# CODIGO C
lista = []
i = 0
while i < 5:
    lista.append(i)
    i += 1
print(lista)

# resposta: todos os codigos A B C dão o mesmo resultado, marquei a alternativa C pois B começava a partir do 1.