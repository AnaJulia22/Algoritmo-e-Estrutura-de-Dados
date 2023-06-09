# Nesse contexto, desenvolva uma função novaLocacao(pilha, codigo) que adiciona, em tempo O(n) o valor inteiro ‘codigo’
# na sua posição apropriada da pilha ‘pilha’ (vetor), se a pilha estiver ordenada.
# A função deve retornar um novo vetor com a nova locação adicionada.
# Mas, atenção, antes disso você deve executar uma função pilhaImaculada(pilha) que checa em tempo O(n) se ela estava
# na ordem certa, antes de fazer a inserção.
#
# Input
#
# A entrada do programa é composta por duas linhas.
# A primeira representa o vetor que se refere à pilha de solicitações, com números inteiros (códigos de locação)
# separados por vírgula e sem espaço, no formato a,b,c.
# A segunda linha é o código da nova locação, que é um inteiro simples
# que deverá ser inserido na lista, se esta estiver ordenada.
#
# Output
#
# Você deve produzir uma única linha de saída. Caso a pilha tenha sido encontrada ordenada e a
# nova solicitação tenha sido inserida nela, deve-se imprimir a nova pilha de solicitações,
# no mesmo formato da entrada (['a','b','c']). Caso a pilha tenha sido encontrada desordenada,
# imprima a expressão “A pilha está um caos.”.

def novaLocacao(pilha, codigo):
    counter = int()
    pilha_ok = False
    for i in range(len(pilha)): 
        if counter == 0:  #se o número ainda não foi adicionado, então compararemos os números
            if pilha[i] > codigo and i == 0: #caso o número a ser adicionado seja menor que o primeiro
                pilha.insert(0, codigo)      #então ele adicionado na posição 0
                counter+=1      #para sinalizar que o número foi adicionado
                pilha_ok = True #depois de ter adicionado o número sinaliza que a pilha agora está ok
            else:
                if pilha[i] > codigo and i != (len(pilha)-1): #se o número a ser adicionado for menor que um número que esteja no meio da pilha
                    pilha.insert(i, codigo)
                    counter+=1
                    pilha_ok = True
                elif pilha[i] > codigo and i == (len(pilha)-1): #se o número a ser adicionado for menor que o último número da pilha
                    pilha.insert(i, codigo)
                    pilha_ok = True
                elif pilha[i] < codigo and i == (len(pilha)-1): #se o número a ser adicionado for maior que todos os números da pilha
                      pilha.insert(i+1, codigo)
                      pilha_ok = True
    if pilha_ok == True:
            return pilha
def pilhaImaculada(pilha):
    check = True
    a = len(pilha) - 1  
    for i in range(len(pilha)):
     if i != a:   #se o i não for a última posição
        antecessor = pilha[i]  #guarda a primeira posição e a próxima para realizar a comparação
        sucessor = pilha[i + 1]
        if check == True:   #se a pilha continua em ordem, isto é, não encontramos nenhuma desordem
            if antecessor <= sucessor: #checa se o número anterior é menor que o seu sucessor, ordem crescente
                check = True
            else:
                check = False
    return check

pilha = (input().split(','))
for i in range(len(pilha)):
    pilha[i] = int(pilha[i])  #transformando os números em inteiros para a comparação poder ser feita
codigo = int(input())
check = pilhaImaculada(pilha)
if check == True: #se a ordem estiver certa
    pilha = (novaLocacao(pilha, codigo))  #chama a função para adicionar a nova solicitação
    for i in range(len(pilha)):
        pilha[i] = str(pilha[i])  #transformando de volta em string para a saída
    print(pilha)
else:   #caso a pilha não estiver ordenada corretamente
    print('A pilha está um caos.')