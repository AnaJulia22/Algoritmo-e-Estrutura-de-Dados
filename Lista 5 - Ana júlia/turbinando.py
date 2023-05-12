class Grafo:
    def add(self, conexao, conexoes, id):
        conexoes[int(id)] = conexao
    def Bfs(self, conexoes, U, alcance, visitado):
        global investimento, a, check      
        fila = []
        fila.append(U)   #adiciona o usuário inicial
        visitado[U] = 1  #marca ele como visitado
        while fila:      
            fila.remove(fila[0]) #remove o primeiro elemento da fila
            for i in conexoes[U]: #percorre os seguidores de um usuário
                if visitado[int(i)] == 0: #se um desses seguidores ainda não foi visitado
                    fila.append(i)       #adiciona ele na fila e adiciona na lista de alcance
                    alcance.append(i)
                    visitado[int(i)] = 1  #marca como visitado
                    if check == True:     #condição para checar se são os seguidores imediatos ou os seguidores dos seguidores
                        a += 1
                        if investimento == a:
                            return
                          
grafo = Grafo()
N = int(input())
U = int(input())
B = float(input())
investimento = int()
a = int()
check = False
alcance = []
visitado = [0]*N
conexoes = [None]*N
counter = int()
while counter != N: #enquanto counter for diferente do número de usuários
    counter += 1      
    conexao = input().split()
    id = conexao[0]   
    conexao.remove(conexao[0]) #remove o id
    conexao.remove(conexao[0]) #remove o :
    if conexao: 
        grafo.add(conexao, conexoes, id) #adiciona os seguidores do id na lista conexoes no indice id
grafo.Bfs(conexoes, U, alcance, visitado) #percorre os seguidores imediatos de id
investimento = int(B//(5.25))  #divide B(o valor investido) por 5,25 para descobrir quantos seguidores dos seguidores poderá ser alcançado
check = True    
for j in alcance:     #percorre a lista alcance até o investimento acabar
    if a == investimento:   #quando a for igual ao investimento, printa a lista alcance
        print(alcance) 
        break
    seguidor = int(j)  #se ainda tiver dinheiro, percorre mais seguidores dos seguidores...
    grafo.Bfs(conexoes, seguidor, alcance, visitado)