class Grafo:
        
    def add (self, conexao, conexoes):   
        #se a posição estiver vazia, apenas subsitui None pela lista 
        if conexoes[conexao[0] - 1] == None:    #0 - 1 porque as posições começam com 0, 1...
            conexoes[conexao[0] - 1] = [conexao[1]]                        
        else: #se já existir uma lista, adiciona um elemento
            conexoes[conexao[0] - 1].append(conexao[1])
            
        if conexoes[conexao[1] - 1] == None:
            conexoes[conexao[1] - 1] = [conexao[0]]
        else:
            conexoes[conexao[1] - 1].append(conexao[0])

    def DfsGrafo(self, N, adj):

        global res

        visitado = [0]*N
        valores = []
        self.Dfs(0, adj, visitado, valores) #percorre as conexões com a primeira vértice
        self.Res(valores)  #depois adiciona numa lista a quantidade de conxões que a vértice tem
        self.nodes_disc(visitado, adj) #percorre os outros vértices soltos
        
    def Dfs(self, node, adj, visitado, valores):

        visitado[node]=1 #marca a vértice como visitada
        valores.append(node+1) #adiciona o valor somado a 1 por causa da posição (0,1...)
        for i in adj[node]: #a lista com as vértices que são conectadas ao node
            if visitado[i-1]==0: #se a vértice ainda não foi visitada
                self.Dfs((i-1),adj,visitado,valores) #Faz a busca com a vértice não visitada
    
    def Res(self, valores): #função para salva a resposta que vai ser printada

        global res

        for i in range(len(valores)):
            #salva na posiçõa da vértice o número de vértices que ele está conectado
            res[valores[i]-1] = len(valores)
            #ex:[1, 7, 4] -> [3,_,_,3,_,_,3]
            #[2,5] -> [3,2,_,3,2,_,3]...

    def nodes_disc (self, visitado, adj):

        for i in range(len(visitado)):
            if visitado[i] == 0:
                valores = []
                self.Dfs(i, adj, visitado, valores)
                self.Res(valores)              

numeros = input().split()
N = int(numeros[0])
M = int(numeros[1])
conexoes = [None]*N
res = [None]*N
grafo = Grafo()    
counter = int()
while counter != M:
    counter += 1
    conexao = input().split()
    conexao = [int(i) for i in conexao]
    grafo.add(conexao, conexoes)
for i in range(len(conexoes)):
    if conexoes[i] == None:  #para vértices que estão sozinhas
        conexoes[i] = [i+1]
grafo.DfsGrafo(N, conexoes)
print(*res)