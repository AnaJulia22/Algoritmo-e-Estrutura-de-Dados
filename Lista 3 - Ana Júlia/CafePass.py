class TabelaHash:
    def __init__(self):
        self.size = 11     
        self.lista = [None] * self.size #criando a lista
    def Insercao(self, num):       #função de inserir os números do cpf na lista
        indice = self.Indice(num)        #descobrindo o indice que o numero será inserido
        if self.lista[indice] is None:   #se o indice estiver vazio, insere o número
            self.lista[indice] = num
        else:                            #caso contrário, procura o próximo lugar vazio
            for lugar in range(self.size):    
                if self.lista[lugar] is None:
                    self.lista[lugar] = num
                    return num
    def Indice(self, elem):    #função para descobrir o indice que o número será inserido 
        return elem % 11       # apartir do módulo da divisão do número em dezena pelo tamanho da lista
    def Dezena(self, num):     #transformando cada número em dezena
        multi = num * 10
        self.Insercao(multi)    #depois que transforma em dezena, chama a função de inserir na lista
    def Soma(self):            #soma os números iguais da lista
        for i in range(11):
            elemA = self.lista[i]
            for j in range(11):
                if (i+j+1) < self.size:
                    elemB = self.lista[i+j+1]
                    if elemA != None and elemB != None:
                        if elemA == elemB:
                            self.lista[i] = self.lista[i] + elemB
                            self.lista[i+j+1] = None
    def Comparar(self, mn):   #comparando a soma dos números com o magic number
        for i in range(11):
            numA = self.lista[i]
            for j in range(11):
                if j != i:
                    numB = self.lista[j]
                    if numA != None and numB != None:
                        if numA + numB == mn:     #se for encontrado uma soma igual ao magic number, print up permission
                            for a in range(self.size):
                                self.lista[a] = None
                            return print('UP Permission')
        else:                                   #caso contrário, printa not permission
            for a in range(self.size):
                self.lista[a] = None
            return print('NOT Permission')
ht = TabelaHash()
N = int(input())        #input pro número de cpf que será inserido
counter = int()
while counter != N:     #while até que o contador seja igual ao número de N
    counter += 1
    numeros = input().split(' ') #separa o cpf do mn
    magic_number = int(numeros[1]) 
    cpf = list(numeros[0])     #separa os números do cpf
    for i in range(len(cpf)): 
        ht.Dezena(int(cpf[i])) 
    ht.Soma()
    ht.Comparar(magic_number)