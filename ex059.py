primeiro: int = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa''')
    opcao = int(input('Qual a sua opção? '))
    if opcao == 1:
        soma = primeiro + segundo
        print(f'Somando: {primeiro} + {segundo} = {soma}.')
    elif opcao == 2:
        multiplicacao = primeiro * segundo
        print(f'Multiplicando: {primeiro} x {segundo} = {multiplicacao}.')
    elif opcao == 3:
        if primeiro > segundo:
            print(f'O número {primeiro} é maior que {segundo}.')
        elif primeiro < segundo:
            print(f'O número {segundo} é maior que {primeiro}.')
        elif primeiro == segundo:
            print(f'{primeiro} e {segundo} são iguais.')
    elif opcao == 4:
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
    print('~-' * 10)
print('Programa encerrado.')