import random
import time

def insertion_sort(balde):
    for i in range(1, len(balde)):
        chave = balde[i]
        j = i - 1
        while j >= 0 and balde[j] > chave:
            balde[j + 1] = balde[j]
            j -= 1
        balde[j + 1] = chave
    return balde

def bucket_sort(lista):
    if len(lista) <= 1:
        return lista[:]
    menor, maior = min(lista), max(lista)
    if menor == maior:
        return lista[:]
    n = len(lista)
    baldes = [[] for _ in range(n)]
    for v in lista:
        baldes[min(int((v - menor) / (maior - menor) * n), n - 1)].append(v)
    return [v for b in baldes for v in insertion_sort(b)]

print("1 - Digitar lista | 2 - Lista aleatória")
if input("Escolha: ") == "1":
    lista = [float(x) for x in input("Números separados por espaço: ").split()]
else:
    lista = [random.randint(0, 1000) for _ in range(int(input("Tamanho: ")))]

inicio = time.perf_counter()
ordenada = bucket_sort(lista)
fim = time.perf_counter()
print("Ordenada:", ordenada if len(ordenada) <= 50 else "(lista grande)")
print(f"Tempo: {fim - inicio:.6f}s")
print("Correto:", ordenada == sorted(lista))
