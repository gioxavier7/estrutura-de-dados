numero = int(input('Digite um número inteiro: '))

print(f'Tabuada do {numero}:')
for i in range(1, 11):
    print(f'{numero} X {i}: {numero * i}')