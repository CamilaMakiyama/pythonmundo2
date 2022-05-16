print('Banco')
valor = int(input('Qual valor você quer sacar? R$'))
nota50 = nota20 = nota10 = nota5 = nota1 = 0
valor1 = 0
nota50 = valor // 50
if nota50 != 0:
    print(f'{nota50} cédula(s) de R$50')
valor1 = valor - (nota50 * 50)
nota20 = valor1 // 20
if nota20 != 0:
    print(f'{nota20} cédula(s) de R$20')
valor2 = valor1 - (nota20 * 20)
nota10 = valor2 // 10
if nota10 != 0:
    print(f'{nota10} cédula(s) de R$10')
valor3 = valor2 - (nota10 * 10)
nota5 = valor3 // 5
if nota5 != 0:
    print(f'{nota5} cédula(s) de R$5')
valor4 = valor3 - (nota5 * 5)
nota1 = valor4 // 1
if nota1 != 0:
    print(f'{nota1} moeda(s) de R$1')
