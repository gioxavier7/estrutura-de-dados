"""
Lista 1 - 30 exercicios (if / elif / else e for)

Cada exercicio foi implementado em uma funcao separada para facilitar estudo.
Quando o enunciado pede entrada do usuario, a funcao usa input().
"""


def ex1():
    n = int(input("Digite um numero inteiro: "))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Zero")


def ex2():
    idade = int(input("Digite a idade: "))
    if idade < 0:
        print("idade invalida")
    elif idade <= 12:
        print("crianca")
    elif idade <= 17:
        print("adolescente")
    else:
        print("adulto")


def ex3():
    a = float(input("Primeiro numero: "))
    b = float(input("Segundo numero: "))
    if a > b:
        print(f"Maior: {a}")
    elif b > a:
        print(f"Maior: {b}")
    else:
        print("Sao iguais")


def ex4():
    nota = float(input("Digite a nota (0 a 10): "))
    if nota < 0 or nota > 10:
        print("Nota invalida")
    elif nota <= 4:
        print("reprovado")
    elif nota <= 6:
        print("exame")
    else:
        print("aprovado")


def ex5():
    n = int(input("Digite um inteiro: "))
    if n % 2 == 0:
        print("Par")
    else:
        print("Impar")


def ex6():
    preco = float(input("Digite o preco do produto: "))
    if preco < 0:
        print("Preco invalido")
        return
    if preco <= 100:
        desconto = 0.05
    elif preco <= 300:
        desconto = 0.10
    else:
        desconto = 0.15
    final = preco * (1 - desconto)
    print(f"Preco final: {final:.2f}")


def ex7():
    a = float(input("Lado 1: "))
    b = float(input("Lado 2: "))
    c = float(input("Lado 3: "))
    if a <= 0 or b <= 0 or c <= 0:
        print("Lados invalidos")
        return
    if a + b <= c or a + c <= b or b + c <= a:
        print("Nao forma triangulo")
    elif a == b == c:
        print("Equilatero")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Escaleno")


def ex8():
    n = int(input("Digite N: "))
    if n < 1:
        print("N deve ser >= 1")
        return
    for i in range(1, n + 1):
        print(i)


def ex9():
    n = int(input("Digite N: "))
    if n < 1:
        print("N deve ser >= 1")
        return
    for i in range(n, 0, -1):
        print(i)


def ex10():
    n = int(input("Digite o numero da tabuada: "))
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def ex11():
    pares = 0
    impares = 0
    for i in range(5):
        n = int(input(f"Digite o {i + 1}o numero: "))
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    print(f"Pares: {pares}")
    print(f"Impares: {impares}")


def ex12():
    n = float(input("Digite o 1o numero: "))
    maior = n
    menor = n
    for i in range(2, 6):
        n = float(input(f"Digite o {i}o numero: "))
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    print(f"Maior: {maior}")
    print(f"Menor: {menor}")


def ex13():
    soma = 0
    for i in range(10):
        n = float(input(f"Digite o {i + 1}o numero: "))
        if n > 0:
            soma += n
    print(f"Soma dos positivos: {soma}")


def ex14():
    n = int(input("Digite N: "))
    if n < 1:
        print("N deve ser >= 1")
        return
    soma = 0
    for i in range(1, n + 1):
        soma += i
    print(f"Somatorio de 1 ate {n}: {soma}")


def ex15():
    n = int(input("Digite N (N >= 0): "))
    if n < 0:
        print("Valor invalido")
        return
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    print(f"{n}! = {fatorial}")


def ex16():
    palavra = input("Digite uma palavra: ").lower()
    vogais = "aeiou"
    total = 0
    for ch in palavra:
        if ch in vogais:
            total += 1
    print(f"Quantidade de vogais: {total}")


def ex17():
    frase = input("Digite uma frase: ").strip()
    if not frase:
        print("Quantidade de palavras: 0")
        return
    palavras = frase.split()
    print(f"Quantidade de palavras: {len(palavras)}")


def ex18():
    notas = []
    for i in range(10):
        nota = float(input(f"Digite a {i + 1}a nota (0 a 10): "))
        while nota < 0 or nota > 10:
            nota = float(input("Nota invalida. Digite novamente (0 a 10): "))
        notas.append(nota)
    media = sum(notas) / len(notas)
    acima = 0
    for nota in notas:
        if nota > media:
            acima += 1
    print(f"Media: {media:.2f}")
    print(f"Notas acima da media: {acima}")


def ex19():
    n = int(input("Digite N: "))
    if n < 1:
        print("N deve ser >= 1")
        return
    for i in range(1, n + 1):
        if i % 3 == 0:
            print(i)


def ex20():
    n = int(input("Digite um inteiro: "))
    if n <= 1:
        print("Nao primo")
        return
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    if primo:
        print("Primo")
    else:
        print("Nao primo")


def ex21():
    n = int(input("Digite N: "))
    if n < 1:
        print("N deve ser >= 1")
        return
    for i in range(1, n + 1):
        print("*" * i)


def ex22():
    n = int(input("Quantos numeros serao lidos? "))
    if n <= 0:
        print("N invalido")
        return
    soma = 0
    qtd = 0
    for i in range(n):
        valor = float(input(f"Digite o {i + 1}o numero: "))
        if 0 <= valor <= 100:
            soma += valor
            qtd += 1
    if qtd == 0:
        print("Nenhum valor valido entre 0 e 100")
    else:
        print(f"Media dos validos: {soma / qtd:.2f}")


def ex23():
    n = int(input("Quantos numeros serao lidos? "))
    if n < 2:
        print("Informe pelo menos 2 numeros")
        return
    primeiro = int(input("Digite o 1o numero: "))
    segundo = int(input("Digite o 2o numero: "))
    maior = max(primeiro, segundo)
    segundo_maior = min(primeiro, segundo)

    for i in range(3, n + 1):
        valor = int(input(f"Digite o {i}o numero: "))
        if valor > maior:
            segundo_maior = maior
            maior = valor
        elif valor > segundo_maior:
            segundo_maior = valor
    print(f"Segundo maior: {segundo_maior}")


def ex24():
    secreto = 37
    tentativas = 5
    for i in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {i}/{tentativas}: "))
        if palpite == secreto:
            print("Acertou!")
            return
        if palpite > secreto:
            print("Palpite maior que o numero secreto")
        else:
            print("Palpite menor que o numero secreto")
    print(f"Nao acertou. O numero era {secreto}.")


def ex25():
    valor_compra = int(float(input("Valor da compra: ")))
    valor_pago = int(float(input("Valor pago: ")))

    if valor_compra < 0 or valor_pago < 0:
        print("Valores invalidos")
        return

    if valor_pago < valor_compra:
        print(f"Saldo devedor: {valor_compra - valor_pago}")
        return

    troco = valor_pago - valor_compra
    print(f"Troco total: {troco}")

    cedulas = [100, 50, 20, 10, 5, 2, 1]
    for valor in cedulas:
        quantidade = troco // valor
        troco %= valor
        if quantidade > 0:
            if valor == 1:
                print(f"{quantidade} moeda(s) de 1")
            else:
                print(f"{quantidade} nota(s) de {valor}")


def ex26():
    nota = float(input("Digite uma nota (0 a 10): "))
    while nota < 0 or nota > 10:
        nota = float(input("Nota invalida. Digite novamente (0 a 10): "))
    print(f"Nota valida: {nota}")


def ex27():
    n = int(input("Quantidade de numeros: "))
    if n < 0:
        print("Quantidade invalida")
        return
    cont_zero = 0
    for i in range(n):
        valor = float(input(f"Digite o {i + 1}o numero: "))
        if valor == 0:
            cont_zero += 1
    print(f"Quantidade de zeros: {cont_zero}")


def ex28():
    n = int(input("Digite N: "))
    if n <= 0:
        print("N deve ser positivo")
        return
    soma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i
    if soma_divisores == n:
        print("Numero perfeito")
    else:
        print("Nao e perfeito")


def ex29():
    palavra = input("Digite uma palavra: ").strip().lower()
    if palavra == palavra[::-1]:
        print("Palindromo")
    else:
        print("Nao e palindromo")


def ex30():
    n = int(input("Quantos termos de Fibonacci? "))
    if n <= 0:
        print("N deve ser positivo")
        return
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


EXERCICIOS = {
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7: ex7,
    8: ex8,
    9: ex9,
    10: ex10,
    11: ex11,
    12: ex12,
    13: ex13,
    14: ex14,
    15: ex15,
    16: ex16,
    17: ex17,
    18: ex18,
    19: ex19,
    20: ex20,
    21: ex21,
    22: ex22,
    23: ex23,
    24: ex24,
    25: ex25,
    26: ex26,
    27: ex27,
    28: ex28,
    29: ex29,
    30: ex30,
}


def menu():
    print("Lista 1 - Escolha o exercicio (1 a 30)")
    numero = int(input("Numero do exercicio: "))
    func = EXERCICIOS.get(numero)
    if func is None:
        print("Exercicio invalido")
    else:
        func()


if __name__ == "__main__":
    menu()
