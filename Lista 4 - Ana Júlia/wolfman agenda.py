def heapSort(arr):       #função para descobrir o min e max com heap
    n = len(arr)   
    for i in range(n // 2 - 1, -1, -1):    #para encontrar o maior número
        largest = i 
        left = 2 * i + 1  
        right = 2 * i + 2 
        if left < n and int(arr[i]) < int(arr[left]): #se left estiver dentro do tamanho da lista,
                                                      #e o elemento do indice i for menor que o elemento do indice left
            largest = left                            #coloca o left como sendo o maior
        if right < n and int(arr[largest]) < int(arr[right]):  #se right for um número que esteja dentro do tamanho da lista e 
                                                               #o maior número atual for menor que o número da direita
            largest = right                            #atualiza o valor do maior
        if largest != i:                               #dps que atualizar o valor de largest, muda a posição do elemento maior
            (arr[i], arr[largest]) = (arr[largest], arr[i])  
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i]) 
        break
    for i in range(n // 2 - 1, -1, -1):     #para encontrar o menor número
        min = i 
        left = 2 * i + 1  
        right = 2 * i + 2 
        if left < n and int(arr[i]) > int(arr[left]):
            min = left  
        if right < n and int(arr[min]) > int(arr[right]):
            min = right  
        if min != i:
            (arr[i], arr[min]) = (arr[min], arr[i])
def jogo(arr, constante):     #função para fazer o cálculo com a constante
    maior = int(arr[-1])
    menor = int(arr[0])
    k = maior - abs(menor * constante)
    if k > 0:              #se k for maior que 0, substitue ele pelo maior número da lista
        arr[-1] = k
    else:                  #caso contrário, só remove  o maior da lista
        arr[-1] = int(maior)
        arr.remove(maior)
sequencia = input().split()
constante = int(input())
counter = int()
while sequencia:      #enquanto a lista sequencia não estiver vazia
    heapSort(sequencia)
    jogo(sequencia, constante)
    counter+=1     #conta o número de rodadas
print(f'{counter} rodadas, partindo para a próxima!')