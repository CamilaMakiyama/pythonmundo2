primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
contador = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo}', end= ' -> ')
        contador += 1
        termo += razao
    mais = int(input('Quantos termos a mais você deseja? '))
print('Fim~')
