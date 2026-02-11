lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

lado_maior = lado1 + lado2

if lado_maior > lado3:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')