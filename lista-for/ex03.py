numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

# comparação entre números
if numero1 > numero2:
    print(f'O número {numero1} é maior que {numero2}.')
elif numero2 > numero1:
    print(f'O número {numero2} é maior que {numero1}.')
else:
    print(f'Os números {numero1} e {numero2} são iguais.')