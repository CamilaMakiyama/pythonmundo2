print('Cadastre Uma Pessoa')
m = 0
menorF = 0
maior = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [F/M]: ')).upper().strip()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        menorF += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas maiores de 18 anos: {maior}.')
print(f'Ao todo temos {m} homens cadastrado(s).')
print(f'E temos {menorF} mulheres menor de 18 anos cadastradas.')