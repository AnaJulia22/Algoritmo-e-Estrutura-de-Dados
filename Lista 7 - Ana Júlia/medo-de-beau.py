def Combinacao(numero, arr, n):
    	
	if n == 0:
		maneiras_possiveis.append(arr)
	else:	
		for i in range(numero, n+1):   
			Combinacao(i, arr + [i], n-i)
			#com a recursão, vai sendo adicionado o numero i na lista 'arr'  
			#até que a soma dos elementos da lista seja igua a n
			#quando o for loop chegar no limite, ele decrementa a quantidade de 1 que seja igual ao i 
			#por exemplo, com um input igual a 5, se i agora é 2, ent a é retirado dois 1s da lista 
			#e assim é adicionado o i, que é 2 e soma continua 5
		return 

  
n = int(input())
maneiras_possiveis = []
arr = []
numero = 1
Combinacao(numero, arr, n)
print(f'Uma sessão com {n} pessoas pode ter sua audiência nos seguintes subgrupos:')
for lista in maneiras_possiveis:
    	
    print(lista)