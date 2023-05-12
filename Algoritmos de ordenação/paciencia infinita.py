def insertion_sort(lista):
    global troca, comparacao, check, contagem
    n = len(lista)
    for j in range(1, n):
        a = int(lista[j])
        i = j - 1
        while i >= 0 and int(lista[i]) > a: 
            comparacao += 1 
            if troca + comparacao >= contagem and check == True:
                return
            lista[i+1] = int(lista[i])
            troca += 1 
            if troca + comparacao >= contagem and check == True:
                return            
            i -= 1 
        if i >= 0:
            comparacao += 1
        lista[i+1] = a
        if troca + comparacao >= contagem and check == True:
            return
        
def shellSort(array):
    global troca, comparacao, check, contagem
    n = len(array)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = int(array[i])
            j = i
            while j >= interval and int(array[j - interval]) > temp:
                comparacao += 1
                if troca + comparacao >= contagem and check == True:
                    return
                array[j] = int(array[j - interval])
                troca += 1                
                j -= interval            
                if troca + comparacao >= contagem and check == True:
                    return
            if int(array[j - interval]) != temp and j>= interval:
                comparacao += 1
            array[j] = temp
            if troca + comparacao >= contagem and check == True:
                return
        interval //= 2

def bubble_sort(lista):
    global troca, comparacao, check, contagem
    n = len(lista)
    for j in range(n-1):
        for i in range(n-j-1):
            comparacao +=1
            if troca + comparacao >= contagem and check == True:
                    return
            if int(lista[i]) > int(lista[i+1]):
                troca += 1                
                lista[i], lista[i+1] = int(lista[i+1]), int(lista[i])
                if troca + comparacao >= contagem and check == True:
                    return

def quicksort(A, lo, hi):
    global troca, comparacao, check, contagem
    if lo >= 0 and hi >= 0 and lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p)
        quicksort(A, p + 1, hi)

def partition(A, lo, hi):
    global troca, comparacao, check, contagem
    pivot = int(A[(hi + lo) // 2])
    i = lo
    j = hi    
    while True:
        if i >= j:
            return j
        while int(A[i]) < pivot:
            comparacao += 1
            if troca + comparacao >= contagem and check == True:
                    return
            i += 1
        while int(A[j]) > pivot:
            comparacao += 1
            if troca + comparacao >= contagem and check == True:
                    return
            j -= 1
        if i <= j:
            A[i], A[j] = int(A[j]), int(A[i])
            troca += 1
            if troca + comparacao >= contagem and check == True:
                    return

def selectionSort(array):
    global troca, comparacao, check, contagem
    n = len(array)   
    for step in range(n):
        min_idx = step
        for i in range(step + 1, n):
            comparacao+=1
            if troca + comparacao >= contagem and check == True:
                    return
            if int(array[i]) < int(array[min_idx]):
                min_idx = i
        if int(array[step]) > int(array[min_idx]):
            (array[step], array[min_idx]) = (int(array[min_idx]), int(array[step]))
            troca += 1
            if troca + comparacao >= contagem and check == True:
                    return

numeros = input().split()
numeros = [int(i) for i in numeros]
troca = int()
comparacao = int()
contagem = int()
check = False

##etapa 1##

lista = list(numeros)
bubble_sort(lista)
print(f'Caça-Rato ordena a lista com {comparacao} comparações e {troca} trocas.')
soma1 = comparacao + troca
troca = comparacao = 0

lista = list(numeros)
selectionSort(lista)
print(f'Grafite ordena a lista com {comparacao} comparações e {troca} trocas.')
soma2 = comparacao + troca
troca = comparacao = 0

lista = list(numeros)
insertion_sort(lista)
print(f'Lacraia ordena a lista com {comparacao} comparações e {troca} trocas.')
soma3 = comparacao + troca
troca = comparacao = 0

lista = list(numeros)
shellSort(lista)
print(f'Rivaldo ordena a lista com {comparacao} comparações e {troca} trocas.')
soma4 = comparacao + troca
troca = comparacao = 0

lista = list(numeros)
quicksort(lista, 0, len(lista)-1)
print(f'Toninho ordena a lista com {comparacao} comparações e {troca} trocas.')
soma5 = comparacao + troca
troca = comparacao = 0

print('-VENCEDOR DA RODADA-')

somas = [soma1, soma2, soma3, soma4, soma5]

min_idx = int()
for i in range(len(somas)):      #for para descobrir a menor soma de ações 
        if i+1 != len(somas):
          if int(somas[i+1]) < int(somas[min_idx]):
            min_idx = i+1
            contagem = somas[min_idx]

if min_idx == 0:
    vencedor = 'Caça-Rato'
elif min_idx == 1:
    vencedor = 'Grafite'
elif min_idx == 2:
    vencedor = 'Lacraia'
elif min_idx == 3:
    vencedor = 'Rivaldo'
elif min_idx == 4:
    vencedor = 'Toninho'

print(f'O vencedor da rodada é {vencedor}, com {contagem} ações.')
print('-Toninho está a dormir...-')
print('Os outros estagiários retornam as seguintes listas com essa quantidade de ações:')

##etapa 2##

check = True
if vencedor != 'Caça-Rato':
    lista = list(numeros)
    bubble_sort(lista)
    print(f'Com {contagem} ações, Caça-Rato ordena a lista assim: {lista}')
    troca = comparacao = 0
if vencedor != 'Grafite':
    lista = list(numeros)
    selectionSort(lista)
    print(f'Com {contagem} ações, Grafite ordena a lista assim: {lista}')
    troca = comparacao = 0
if vencedor != 'Lacraia':
    lista = list(numeros)
    insertion_sort(lista)
    print(f'Com {contagem} ações, Lacraia ordena a lista assim: {lista}')
    troca = comparacao = 0
if vencedor != 'Rivaldo':
    lista = list(numeros)
    shellSort(lista)
    print(f'Com {contagem} ações, Rivaldo ordena a lista assim: {lista}')