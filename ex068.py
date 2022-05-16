import random
from random import randint
print('Vamos Jogar Par ou Ímpar')
v = 0
while True:
    print('*~'*20)
    valor = int(input('Diga um valor: '))
    computador = random.randint(0, 10)
    soma = computador + valor
    PouI = str(input('Par ou Ímpar? [P/I]: ')).upper().strip()[0]
    print('*~' * 20)
    if PouI in 'P':
        if soma % 2 == 0:
            print(f'Você escolheu {valor} e o computador {computador}. A soma deu {soma}. ')
            print('Resultado: Par')
            print('Parabéns você ganhou!')
            v += 1
        else:
            print(f'Você escolheu {valor} e o computador {computador}. A soma deu {soma}. ')
            print('Resultado: Ímpar')
            print('Você perdeu')
            break
    elif PouI in 'IÍ':
        if soma % 2 != 0:
            print(f'Você escolheu {valor} e o computador {computador}. A soma deu {soma}. ')
            print('Resultado: Ímpar')
            print('Parabéns você ganhou!')
            v += 1
        else:
            print(f'Você escolheu {valor} e o computador {computador}. A soma deu {soma}. ')
            print('Resultado: Par')
            print('Você perdeu!')
            break
print(f'Número de vezes que você venceu: {v}')
print('Obrigada por Jogar <3')
