peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}. Abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f}. Peso ideal.')
elif imc < 30:
    print (f'Seu IMC é {imc:.2f}. Sobrepeso.')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f}. Obesidade.')
else:
    print(f'Seu IMC é {imc:.2f}. Obesidade mórbida.')
