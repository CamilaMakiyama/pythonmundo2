print('Sequência de Fibonacci')
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = 0
print(f'{t1} -> {t2}', end= '')
contador = 3
while contador <= n:
    contador += 1
    t3 = t1 + t2
    print(f' -> {t3}', end= '')
    t1 = t2
    t2 = t3
print('Fim~')