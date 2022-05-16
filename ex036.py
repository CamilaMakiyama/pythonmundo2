casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Digite em quantos anos você quer pagar essa casa: '))
parcela = casa / (anos*12)
minimo = salario*0.3
print(f'Uma casa de R${casa:.2f} gerará uma prestação de R${parcela:.2f} em {anos} anos.')
if parcela <= minimo:
    print(f'Empréstimo concedido com sucesso!')
else:
        print(f'Empréstimo negado! É necessário que a parcela seja no máximo 30% do seu salário.')