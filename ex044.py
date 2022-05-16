preco = float(input('Preço das compras: R$'))
pagamento = int(input('''Formas de Pagamento:
[ 1 ] à vista no dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Sua opção: '''))
if pagamento == 1:
    valor = preco - (preco * 0.10)
    print(f'Sua compra de {preco:.2f}, vai custar {valor:.2f} no final.')
elif pagamento == 2:
    valor = preco - (preco *0.05)
    print(f'Sua compra de {preco:.2f}, vai custar {valor:.2f} no final.')
elif pagamento == 3:
    parcelas = preco / 2
    print(f'Sua compra será parcelada em 2x de R${parcelas}.')
    print(f'Sua compra continuará com o valor de {preco:.2f}.')
else:
    valor = preco + (preco * 0.20)
    qparcelas = int(input('Digite o número de parcelas: '))
    parcelas = valor / qparcelas
    print(f'Sua compra será parcelada em {qparcelas}x de R${parcelas} com juros.')
    print(f'Sua compra de {preco:.2f}, vai custar {valor:.2f} no final.')
