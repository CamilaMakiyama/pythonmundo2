numero = int(input('Digite um número: '))
contador = 0
for c in range (1,numero+1):
    if (numero % c) == 0:
        contador += 1
        print('\033[33m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    print(f'{c}')
print(f'O número foi divisível {contador} vezes.')
if contador == 2:
    print('Por isso ele é um número primo.')
else:
    print('Por isso ele não é um número primo.')