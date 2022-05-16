import random
print('''Olá, sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar?''')
adivinha = int(input('Qual seu palpite? '))
numero = random.randint(1, 10)
contador = 1
while adivinha != numero:
    if adivinha < numero:
        adivinha = int(input('''
Não... tente novamente. 
Dica: é mais
Qual seu palpite? '''))
        contador += 1
    elif adivinha > numero:
        adivinha = int(input('''
Não... tente novamente. 
Dica: é menos
Qual seu palpite? '''))
        contador += 1
print(f'Você acertou com {contador} tentativas. Parabéns. ')