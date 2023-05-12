def mergeSort(lista1, lista2):
    lista = []
    if len(lista1) > 1:
        left = lista1
        right = lista2
        i = int()
        j = int()
        while i < len(left) and j < len(right):
            if int(left[i]) <= int(right[j]): #se o elemento do indice i da lista 1 for menor que o elemento do inidce j da lista 2
                lista.append(int(left[i]))    #adiciona o elemento da lista 1 na nova lista
                i += 1
            else:                             #caso contrário, adiciona o da lista 2
                lista.append(int(right[j]))
                j += 1
        while i < len(left):                 #verifica  se ainda existem elementos na lista 1, se sim, adiciona o restante
            lista.append(int(left[i]))
            i += 1
        while j < len(right):              #se sobrar na lista 2, adiciona os restantes
            lista.append(int(right[j]))
            j += 1
        return lista
    
salario_sport = input().split()
salario_clube = input().split()
salarios = mergeSort(salario_sport, salario_clube)
a = len(salarios) % 2
if a == 0:              #checa se a lista tem um número par ou impar de elementos
        meio = len(salarios) // 2          #se for par, pega os dois elementos do meio e divide por dois 
        mediana = (salarios[meio-1] + salarios[meio])/2
else:
        meio = (len(salarios) // 2) + 1          #se for impar, basta pegar o elemento do meio
        mediana = salarios[meio] 
print(f'O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais.')