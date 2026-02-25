preco = float(input('Digite o preço do produto: R$ '))

#verificando os descontos
if preco <= 100:
    desconto = 0.05
elif preco <= 300:
    desconto = 0.10
else:
    desconto = 0.15

#aplicando o respectivo desconto no preço final do produto
preco_final = preco * (1 - desconto)

print(f'Preço final com desconto: R$ {preco_final:.2f}')