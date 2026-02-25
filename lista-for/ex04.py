nota = float(input('Digite sua nota: '))

# condicionais das notas
if nota >= 6:
    print('Aprovado.')
elif nota >= 4.1 and nota < 6:
    print('Em exame.')
else:
    print('Reprovado.')