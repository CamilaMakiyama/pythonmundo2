sexo = str(input('Informe seu sexo: [F/M]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informe seu sexo: [F/M]')).strip().upper()[0]
print(f'Sexo {sexo} registrado.')