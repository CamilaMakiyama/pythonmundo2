from math import factorial
numero = int(input('Digite o número que deseja calcular o fatorial: '))
fatorial = factorial(numero)
c = numero
print(f'Calculando... {numero}!')
while c > 0:
    print(f'{c}')
    print('x' if c > 1 else f'= {fatorial}')
    c-=1
