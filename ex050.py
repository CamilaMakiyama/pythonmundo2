acum = 0
for c in range(0,6):
    numero = int(input('Digite um número: '))
    if (numero % 2) == 0:
        acum += numero
print(f'A soma dos números pares é: {acum}.')