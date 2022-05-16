cont = 0
while True:
    tabuada = int(input('Deseja ver a tabuada de qual valor? '))
    cont = 0
    if tabuada < 0:
        break
    while cont < 11:
        resultado = tabuada * cont
        print(f'{tabuada} x {cont} = {resultado}')
        cont += 1
print('Tabuada encerrada.')

while True:
    t = int(input('Deseja ver a tabuada de qual valor? '))
    if t < 0:
        break
    for c in range (1,11):
        print(f'{t} x {c} = {t*c}')
print('Tabuada encerrada.')