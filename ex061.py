primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
c = 1
while c <= 10:
    print(f'{termo}', end= '->')
    termo +=razao
    c += 1
print('Fim')