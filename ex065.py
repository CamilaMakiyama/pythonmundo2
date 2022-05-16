sn = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
while sn in 'Ss':
    numero = int(input('Digite um número: '))
    cont += 1
    soma += numero
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    sn = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma/cont
print (f'Você digitou {cont} números e a média foi {media}.')
print(f'O maior valor foi {maior} e o menor foi {menor}.')