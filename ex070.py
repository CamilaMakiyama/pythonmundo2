print ('~Loja~')
menor = 100000
maior = 0
produtomenor = ' '
soma = 0
cont = 0
while True:
    produto = str(input('Nome do Produto: ')).strip()
    valor = float(input('Qual o valor? R$'))
    soma += valor
    if valor < menor:
        menor = valor
        produtomenor = produto
    if valor > 1000:
        cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
print(f'O total da compra foi R${soma}.')
print(f'Temos {cont} produto(s) custando mais de R$1000.00.')
print(f'O produto mais barato foi {produtomenor} que custa {menor}.')