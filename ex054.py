contador = 0
contador2 = 0
for c in range (1,8):
    idade = int(input(f'Digite o ano da {c} pessoa: '))
    if idade <= 2004:
        contador += 1
    else:
        contador2 += 1
print(f'Temos {contador} maiores de idade e {contador2} menores de idade.')