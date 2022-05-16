soma = 0
cont = 0
for c in range(0,501):
    if (c%3) == 0 and (c%2) != 0:
        soma+=c
        cont+=1
print(f'A soma de {cont} valores solicitados é de {soma}.')
