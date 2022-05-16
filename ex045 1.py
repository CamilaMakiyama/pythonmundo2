import random
from time import sleep
print('''Jokenpo 
[1] Pedra
[2] Papel
[3] Tesoura''')
jogador1 = int(input('Escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
jogador2 = random.randint(1,3)
print('~~'*20)
if jogador1 == 1:
    print('Você escolheu Pedra.')
    if jogador2 == 1:
        print('O programa escolheu Pedra.\nResultado: Empate!')
    elif jogador2 == 2:
        print('O programa escolheu Papel.\nResultado: Você perdeu!')
    else:
        print(f'O programa escolheu Tesoura.\nResultado: Você ganhou!')
if jogador1 == 2:
    print('Você escolheu Papel.')
    if jogador2 == 1:
        print(f'O programa escolheu Pedra.\nResultado: Você ganhou!')
    elif jogador2 == 2:
        print('O programa escolheu Papel.\nResultado: Empate!')
    else:
        print('O programa escolheu Tesoura.\nResultado: Você perdeu!')
if jogador1 == 3:
    print('Você escolheu Tesoura.')
    if jogador2 == 1:
        print('O programa escolheu Pedra.\nResultado: Você perdeu!')
    elif jogador2 == 2:
        print(f'O programa escolheu Papel.\nResultado: Você ganhou!')
    else:
        print('O programa escolheu Tesoura.\nResultado: Empate!')
print('~~'*20)