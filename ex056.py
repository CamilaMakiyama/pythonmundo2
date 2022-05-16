midade = 0
menoresde20 = 0
maior = 0
for dados in range (1,5):
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [F/M]: ')).lower()
    midade += idade
    if sexo == 'm':
        if dados == 1:
            maior = idade
        else:
            if idade > maior:
                velho = nome
    else:
        if idade < 20:
            menoresde20 += 1
media = midade/4
print(f'O nome do homem mais velho do grupo é {velho}.')
print(f'A média de idade do grupo é de {media} anos.')
print(f'Temos {menoresde20} mulheres com menos de 20 anos.')
