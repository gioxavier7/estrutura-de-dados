lado1 = int(input('Digite um valor para o lado 1: '))
lado2 = int(input('Digite um valor para o lado 2: '))
lado3 = int(input('Digite um valor para o lado 3: '))

#verificando se é ou não um triângulo
if lado1 + lado2 > lado3 and lado2 + lado3 > lado2 and lado2 + lado3 > lado1:
    #descobrindo o tipo de triângulo
    if lado1 == lado2 == lado3:
        print('Equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isósceles.')
    else:
        print('Escaleno.')
else:
    print('Com os valores passados, não é possível formar um triângulo.')