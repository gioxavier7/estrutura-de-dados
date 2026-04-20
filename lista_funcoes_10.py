"""
Lista de Exercicios - Funcoes
"""


def dobro(numero):
    return numero * 2


def area_retangulo(base, altura):
    return base * altura


def media_tres(n1, n2, n3):
    return (n1 + n2 + n3) / 3


def maior_entre_dois(a, b):
    if a >= b:
        return a
    return b


def verifica_intervalo(numero):
    if 10 <= numero <= 50:
        return "Dentro do intervalo"
    return "Fora do intervalo"


def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    cont = 0
    for ch in texto:
        if ch in vogais:
            cont += 1
    return cont


def soma_lista(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma


def multiplicar_lista(lista):
    produto = 1
    for valor in lista:
        produto *= valor
    return produto


def eh_multiplo(a, b):
    if b == 0:
        return False
    return a % b == 0


def contador_regressivo(n):
    if n < 0:
        print("Valor invalido")
        return
    for i in range(n, -1, -1):
        print(i)


def menu():
    print("Lista de Funcoes - 10 exercicios")
    print("1) dobro")
    print("2) area_retangulo")
    print("3) media_tres")
    print("4) maior_entre_dois")
    print("5) verifica_intervalo")
    print("6) contar_vogais")
    print("7) soma_lista")
    print("8) multiplicar_lista")
    print("9) eh_multiplo")
    print("10) contador_regressivo")
    op = int(input("Escolha: "))

    if op == 1:
        n = float(input("Numero: "))
        print(dobro(n))
    elif op == 2:
        b = float(input("Base: "))
        h = float(input("Altura: "))
        print(area_retangulo(b, h))
    elif op == 3:
        n1 = float(input("N1: "))
        n2 = float(input("N2: "))
        n3 = float(input("N3: "))
        print(media_tres(n1, n2, n3))
    elif op == 4:
        a = float(input("A: "))
        b = float(input("B: "))
        print(maior_entre_dois(a, b))
    elif op == 5:
        numero = float(input("Numero: "))
        print(verifica_intervalo(numero))
    elif op == 6:
        texto = input("Texto: ")
        print(contar_vogais(texto))
    elif op == 7:
        entrada = input("Numeros separados por espaco: ").strip().split()
        lista = [float(x) for x in entrada]
        print(soma_lista(lista))
    elif op == 8:
        entrada = input("Numeros separados por espaco: ").strip().split()
        lista = [float(x) for x in entrada]
        print(multiplicar_lista(lista))
    elif op == 9:
        a = int(input("A: "))
        b = int(input("B: "))
        print(eh_multiplo(a, b))
    elif op == 10:
        n = int(input("N: "))
        contador_regressivo(n)
    else:
        print("Opcao invalida")


if __name__ == "__main__":
    menu()
