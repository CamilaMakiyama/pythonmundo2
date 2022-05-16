s = cont = 0
while True:
    numero = int(input('Digite um valor (1000 para parar): '))
    if numero == 1000:
        break
    s += numero
    cont += 1
print(f'A soma dos {cont} é {s}.')

soma = 0
cont = 0
while True:
    valor = int(input('Digite um valor (999 para parar): '))
    if valor == 999:
        break
    soma += valor
    cont += 1
print(f'A soma dos {cont} valores é de {soma}.')
