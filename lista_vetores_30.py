"""
Lista de Vetores
"""


def ex1():
    lista = []
    lista.append(10)
    print(lista)


def ex2():
    lista = []
    for n in [5, 3, 8, 6, 1]:
        lista.append(n)
    print(lista)


def inserir_valor(lista, valor):
    lista.append(valor)
    return lista


def pesquisa_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def remover_primeira_ocorrencia(lista, alvo):
    novo = []
    removido = False
    for valor in lista:
        if valor == alvo and not removido:
            removido = True
            continue
        novo.append(valor)
    return novo


def inserir_ordenado(lista, valor):
    nova = []
    inserido = False
    for atual in lista:
        if not inserido and valor <= atual:
            nova.append(valor)
            inserido = True
        nova.append(atual)
    if not inserido:
        nova.append(valor)
    return nova


def ex7():
    lista = []
    for i in range(1, 11):
        lista.append(i)
    print(lista)


def inverter_lista(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida


def soma_elementos(lista):
    total = 0
    for valor in lista:
        total += valor
    return total


def maior_elemento(lista):
    if not lista:
        return None
    maior = lista[0]
    for valor in lista[1:]:
        if valor > maior:
            maior = valor
    return maior


def menor_elemento(lista):
    if not lista:
        return None
    menor = lista[0]
    for valor in lista[1:]:
        if valor < menor:
            menor = valor
    return menor


def contar_ocorrencias(lista, alvo):
    cont = 0
    for valor in lista:
        if valor == alvo:
            cont += 1
    return cont


def filtrar_pares(lista):
    pares = []
    for valor in lista:
        if valor % 2 == 0:
            pares.append(valor)
    return pares


def quadrado_elementos(lista):
    nova = []
    for valor in lista:
        nova.append(valor * valor)
    return nova


def contem_elemento(lista, alvo):
    for valor in lista:
        if valor == alvo:
            return True
    return False


def remover_duplicados(lista):
    nova = []
    for valor in lista:
        if not contem_elemento(nova, valor):
            nova.append(valor)
    return nova


def inserir_se_nao_existir(lista, valor):
    if not contem_elemento(lista, valor):
        lista.append(valor)
    return lista


def combinar_listas(lista1, lista2):
    nova = []
    for valor in lista1:
        nova.append(valor)
    for valor in lista2:
        nova.append(valor)
    return nova


def inverter_lista_2(lista):
    return lista[::-1]


def calcular_media(lista):
    if not lista:
        return 0
    return soma_elementos(lista) / len(lista)


def segundo_maior(lista):
    unicos = remover_duplicados(lista)
    if len(unicos) < 2:
        return None
    maior = unicos[0]
    segundo = None
    for valor in unicos[1:]:
        if valor > maior:
            segundo = maior
            maior = valor
        elif segundo is None or valor > segundo:
            segundo = valor
    return segundo


def indice_primeiro_maior_que(lista, limite):
    for i in range(len(lista)):
        if lista[i] > limite:
            return i
    return -1


def interseccao_sem_duplicatas(lista1, lista2):
    comum = []
    for valor in lista1:
        if contem_elemento(lista2, valor) and not contem_elemento(comum, valor):
            comum.append(valor)
    return comum


def contar_impares(lista):
    cont = 0
    for valor in lista:
        if valor % 2 != 0:
            cont += 1
    return cont


def indices_ocorrencia(lista, alvo):
    indices = []
    for i in range(len(lista)):
        if lista[i] == alvo:
            indices.append(i)
    return indices


def duplicar_elementos(lista):
    nova = []
    for valor in lista:
        nova.append(valor)
        nova.append(valor)
    return nova


def selection_sort(lista):
    ordenada = lista[:]
    n = len(ordenada)
    for i in range(n):
        idx_menor = i
        for j in range(i + 1, n):
            if ordenada[j] < ordenada[idx_menor]:
                idx_menor = j
        ordenada[i], ordenada[idx_menor] = ordenada[idx_menor], ordenada[i]
    return ordenada


def remover_primeiro_ultimo(lista):
    if len(lista) <= 2:
        return []
    return lista[1:-1]


def lista_vazia(lista):
    return len(lista) == 0


def soma_dois_vetores(v1, v2):
    if len(v1) != len(v2):
        return None
    soma = []
    for i in range(len(v1)):
        soma.append(v1[i] + v2[i])
    return soma


def menu_demo():
    print("Exemplos rapidos da lista de vetores:")
    ex1()
    ex2()
    ex7()
    print(inserir_valor([1, 2], 3))
    print(pesquisa_linear([10, 20, 30], 20))
    print(remover_primeira_ocorrencia([1, 2, 3, 2], 2))
    print(inserir_ordenado([1, 3, 5], 4))
    print(inverter_lista([1, 2, 3]))
    print(soma_elementos([1, 2, 3]))
    print(maior_elemento([5, 9, 1]))
    print(menor_elemento([5, 9, 1]))
    print(contar_ocorrencias([1, 2, 2, 3], 2))
    print(filtrar_pares([1, 2, 3, 4]))
    print(quadrado_elementos([2, 3, 4]))
    print(contem_elemento([1, 2, 3], 2))
    print(remover_duplicados([1, 2, 2, 3, 1]))
    print(inserir_se_nao_existir([1, 2], 2))
    print(combinar_listas([1], [2, 3]))
    print(inverter_lista_2([1, 2, 3]))
    print(calcular_media([2, 4, 6]))
    print(segundo_maior([10, 8, 10, 7]))
    print(indice_primeiro_maior_que([1, 3, 6], 4))
    print(interseccao_sem_duplicatas([1, 2, 3], [2, 3, 4]))
    print(contar_impares([1, 2, 3, 4, 5]))
    print(indices_ocorrencia([1, 2, 1, 3, 1], 1))
    print(duplicar_elementos([7, 8]))
    print(selection_sort([5, 3, 1, 4]))
    print(remover_primeiro_ultimo([1, 2, 3, 4]))
    print(lista_vazia([]))
    print(soma_dois_vetores([1, 2, 3], [4, 5, 6]))


if __name__ == "__main__":
    menu_demo()
