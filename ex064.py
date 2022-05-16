numero = int(input('Digite um número [999 para parar]: '))
quantidade = 0
soma = 0
while numero != 999:
    quantidade += 1
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}.')