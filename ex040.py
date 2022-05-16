nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1+nota2)/2
if media >= 7.00:
    print(f'Sua média é de {media:.2f}, portanto você está APROVADO.')
elif media < 5.00:
    print(f'Sua média é de {media:.2f}, portanto você está REPROVADO.')
else:
    print(f'Sua média foi de {media:.2f}, portanto você está de RECUPERAÇÃO.')
