frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto [::-1]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não é um palíndromo.')