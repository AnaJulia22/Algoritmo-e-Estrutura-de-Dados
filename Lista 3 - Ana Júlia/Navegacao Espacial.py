class TabelaHash:
    def __init__(self, N):
        self.size = N
        self.lista = [None] * self.size
    def ADD(self, num):                    #função para adicionar um numero
        posicao = self.Indice(num)         #pega o resto da divisão do numero por N para saber onde ele deve ser adicionado
        if self.lista[posicao] is None:    #se a posição estiver vazia, adiciona o número normalmente
            self.lista[posicao] = num 
            return print(f'E: {posicao}')
        else:                               #caso a posição já esteja preenchida
            if self.lista[posicao] != num:     
                for i in range(posicao, self.size):    #verifica uma posição vazia logo após a posição que ele deveria ter sido adicionado
                     if self.lista[i] is None:
                        self.lista[i] = num
                        return print(f'E: {i}')
                for i in range(posicao):            #caso não tenha mais posições vazias posteriores, verifica posições anteriores 
                    if self.lista[i] is None:
                        self.lista[i] = num
                        return print(f'E: {i}')
    def Indice(self, elem):      #função para descobrir a posição a partir do mod
        return elem % N
    def SCH(self, num):          #funçõa de pesquisa do número
        posicao = self.Indice(num)
        if self.lista[posicao] == num:         #se ele estiver na posição esperada, printa normal
            return print(f'E: {posicao}')
        else:                                  #caso contrário, será necessário fazer uma pesquisa até encontrá-lo
            for i in range(self.size):
                if self.lista[i] == num:
                    return print(f'E: {i}')
            return print('NE')
    def CAP(self, posicao):     #função para printar o elemento dado uma posição
        if self.lista[posicao] is None:
            print('D')          #se a posição dada estiver vazia
        else:                   #se não estiver, printa o numero que esteja nela
            print(f'A: {self.lista[posicao]}')
    def EspacoVazio(self):      #função para verificar se ainda há alguma posição vazia
        contador = int()
        for i in range(self.size):
            if self.lista[i] is not None:
                contador +=1
        if contador == self.size:
            return True
        return False
N = int(input())
ht = TabelaHash(N)
C = int(input())
counter = int()
no_space = False
while counter != C: #até que o contador seja igual a C = número de linhas a serem dadas
    counter+=1
    comando = input().split(' ')
    if comando[0] == 'ADD':
        ht.ADD(int(comando[1]))
    elif comando[0] == 'CAP':
        ht.CAP(int(comando[1]))
    elif comando[0] == 'SCH':
        ht.SCH(int(comando[1]))
    no_space = ht.EspacoVazio()  #chama a função para verificar se ainda tem alguma posição vazia
    if no_space == True:  #caso não tenha
        print('Toda memoria utilizada')
        counter = C    #iguala o counter ao C para finalizar o While