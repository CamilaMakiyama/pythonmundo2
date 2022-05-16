num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para a conversão: 
(1) Converter para binário
(2) Converter para octal
(3) Converter para hexadecimal''')
escolha = int(input('Sua escolha: '))
if escolha == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}.')
elif escolha == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}.')
else:
    print(f'{num} convertido para hexadecimal {hex(num)[2:]}.')
