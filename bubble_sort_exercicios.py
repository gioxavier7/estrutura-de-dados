"""
Exercicios de Bubble Sort
"""

import random
import time


def bubble_sort(lista):
    arr = lista[:]
    n = len(arr)
    comparacoes = 0
    trocas = 0
    passos = []

    for i in range(n - 1):
        troca_ocorreu = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
                troca_ocorreu = True
        passos.append(arr[:])
        if not troca_ocorreu:
            break
    return arr, comparacoes, trocas, passos


def ex1():
    v = [5, 3, 8, 1, 2]
    ordenado, comparacoes, trocas, passos = bubble_sort(v)
    print("Exercicio 1")
    print("Inicial:", v)
    for i, estado in enumerate(passos, start=1):
        print(f"Iteracao {i}: {estado}")
    print("Final:", ordenado)
    print("Comparacoes:", comparacoes, "Trocas:", trocas)


def ex2():
    v = [1, 2, 3, 4, 5]
    ordenado, comparacoes, trocas, passos = bubble_sort(v)
    print("Exercicio 2")
    print("Inicial:", v)
    for i, estado in enumerate(passos, start=1):
        print(f"Iteracao {i}: {estado}")
    print("Final:", ordenado)
    print("Comparacoes:", comparacoes, "Trocas:", trocas)


def ex3():
    v = [9, 7, 5, 3, 1]
    ordenado, comparacoes, trocas, passos = bubble_sort(v)
    print("Exercicio 3")
    print("Inicial:", v)
    for i, estado in enumerate(passos, start=1):
        print(f"Iteracao {i}: {estado}")
    print("Final:", ordenado)
    print("Comparacoes:", comparacoes, "Trocas:", trocas)


def ex4():
    v = [4, 2, 4, 1, 3]
    ordenado, comparacoes, trocas, passos = bubble_sort(v)
    print("Exercicio 4")
    print("Inicial:", v)
    for i, estado in enumerate(passos, start=1):
        print(f"Iteracao {i}: {estado}")
    print("Final:", ordenado)
    print("Comparacoes:", comparacoes, "Trocas:", trocas)
    print("Observacao: elementos iguais mantem ordem relativa (estavel).")


def ex5():
    v = [2, 1, 3, 4, 5]
    ordenado, comparacoes, trocas, passos = bubble_sort(v)
    print("Exercicio 5 (com otimizacao de parada antecipada)")
    print("Inicial:", v)
    for i, estado in enumerate(passos, start=1):
        print(f"Iteracao {i}: {estado}")
    print("Final:", ordenado)
    print("Comparacoes:", comparacoes, "Trocas:", trocas)


def ex6():
    notas = [7.5, 9.2, 6.0, 8.3, 5.5]
    ordenado, comparacoes, trocas, _ = bubble_sort(notas)
    print("Exercicio 6")
    print("Notas ordenadas:", ordenado)
    print("Menor nota:", ordenado[0])
    print("Maior nota:", ordenado[-1])
    print("Comparacoes:", comparacoes, "Trocas:", trocas)


def ex7():
    produtos = [
        {"nome": "Arroz", "preco": 20},
        {"nome": "Feijao", "preco": 12},
        {"nome": "Macarrao", "preco": 5},
    ]
    precos = [p["preco"] for p in produtos]
    ordenado, _, _, _ = bubble_sort(precos)
    print("Exercicio 7")
    print("Precos originais:", precos)
    print("Precos ordenados:", ordenado)


def ex8():
    lista = [random.randint(1, 10_000) for _ in range(1000)]
    copia = lista[:]

    inicio = time.time()
    bubble_sort(lista)
    tempo_bubble = time.time() - inicio

    inicio = time.time()
    copia.sort()
    tempo_sort = time.time() - inicio

    print("Exercicio 8")
    print(f"Tempo bubble_sort: {tempo_bubble:.6f} s")
    print(f"Tempo sort() Python: {tempo_sort:.6f} s")


def menu():
    print("Bubble Sort - escolha o exercicio (1 a 8)")
    op = int(input("Opcao: "))
    if op == 1:
        ex1()
    elif op == 2:
        ex2()
    elif op == 3:
        ex3()
    elif op == 4:
        ex4()
    elif op == 5:
        ex5()
    elif op == 6:
        ex6()
    elif op == 7:
        ex7()
    elif op == 8:
        ex8()
    else:
        print("Opcao invalida")


if __name__ == "__main__":
    menu()
