from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'O atleta possui {idade} e está na categoria mirim.')
elif idade <= 14:
    print(f'O atleta possui {idade} e está na categoria infantil.')
elif idade <= 19:
    print(f' O atleta tem {idade} e está na categoria júnior.')
elif idade <= 25:
    print(f'O atleta tem {idade} e está na categoria sênior.')
else:
    print(f'O atleta tem {idade} e está na categoria master.')
