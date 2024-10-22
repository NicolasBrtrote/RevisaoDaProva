def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = 70.2
altura = 1.62

imc = calcular_imc(peso, altura)

print(f"O seu IMC é: {imc:.2f}")

if imc < 17:
    print("Muito abaixo do peso")
elif 17 <= imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Peso Normal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 35:
    print("Obesidade Grau I")
elif 35 <= imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")


# saída: O seu IMC é: 26.75 Sobrepeso