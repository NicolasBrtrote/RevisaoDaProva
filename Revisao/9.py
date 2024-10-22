alpha = float(input('Informe alpha: '))
x = float(input('Informe X: '))
if alpha > 0.1:
    print('Valor inválido para alpha')
else:
    if x < 0:
        print(alpha * x)
    else:
        print(x)


# Para alpha > 0.1, ele retorna uma mensagem de erro.
# Para alpha <= 0.1 e x < 0, ele retorna o produto de alpha e x.
# Para alpha <= 0.1 e x >= 0, ele retorna o valor de x.
# Não sabia muito bem o que fazer então tentei fazer de um jeito meio sem sentido.
