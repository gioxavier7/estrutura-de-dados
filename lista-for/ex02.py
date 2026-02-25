idade = int(input('Digite sua idade: '))

# verificação de idade
if idade < 0:
    print('Idade inválida.')
elif idade >= 0 and idade <= 12:
    print('Criança.')
elif idade >= 13 and idade <= 17:
    print('Adolescente.')
else:
    print('Adulto.')