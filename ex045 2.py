import random
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
jogador2 = random.randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador1 = int(input('Escolha: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')
sleep(1)
print('~~'*20)
print(f'Você jogou {itens[jogador1]}.')
print(f'O programa jogou {itens[jogador2]}.')
if jogador1 == 0:
    if jogador2 == 0:
        print('Empate.')
    elif jogador2 == 1:
        print('Você perdeu!')
    else:
        print('Você ganhou!')
if jogador1 == 1:
    if jogador2 ==0 :
        print('Você ganhou!')
    elif jogador2 == 1:
        print('Empate.')
    else:
        print('Você perdeu!')
if jogador1 == 2:
    if jogador2 == 0:
        print('Você perdeu!')
    elif jogador2 == 1:
        print('Você ganhou!')
    else:
        print('Empate.')
print('~~' * 20)