numeros = []

for i in range(5):
    num = int(input(f'Digite o {i + 1}º número: '))
    numeros.append(num)

numeros.sort()
print('Números em ordem crescente:')
print(numeros)