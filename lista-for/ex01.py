numero = int(input("Digite um número inteiro: "))

# verificação se número é positivo, negativo ou 0
if numero >= 1:
    print(f'O número {numero} é positivo.')
elif numero < 0:
    print(f'O número {numero} é negativo.')
else:
    print(f'O número {numero} é igual a 0.')