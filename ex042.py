r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2 and r2 == r3:
         print('Triângulo equilátero.')
    elif r1 == r2 and r2 != r3 or r1 == r3 and r1 != r2 or r2 == r3 and r3 != r1:
         print('Triângulo esósceles.')
    elif r1 != r2 and r2 != r3:
        print('Triângulo escaleno.')
else:
    print('Não é possível formar um triângulo com esses segmentos.')
