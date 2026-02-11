num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
num3 = float(input('Digite o terceiro valor: '))

if num1 > num2 and num1 > num3:
    print(f'O número {num1} é maior.')
elif num2 > num1 and num2 > num3:
    print(f'O número {num2} é o maior.')
else:
    print(f'O número {num3} é o maior.')