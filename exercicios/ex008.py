num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if num1 == num2:
    print(f'Os números {num1} e {num2} são iguais.')
elif num1 > num2:
    print(f'O número {num1} é maior que {num2}')
else:
    print(f'O número {num2} é maior que {num1}')