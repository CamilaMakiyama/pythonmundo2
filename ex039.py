from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
atual = date.today().year
idade = atual - ano
if ano == 2004:
    print(f'Quem nasceu em {ano}, tem 18 anos em 2022.')
    print(f'Precisa se alistar imediatamente.')
elif ano < 2004:
    print(f'Quem nasceu em {ano}, tem {idade} em 2022.')
    alistamento = 2022 - (idade - 18)
    print(f'Deveria ter se alistado em {alistamento}.')
else:
    print(f'Quem nasceu em {ano}, tem {idade} em 2022. ')
    alistamento2 = 2022 + (18 - idade)
    print(f'Deverá se alistar em {alistamento2}.')
