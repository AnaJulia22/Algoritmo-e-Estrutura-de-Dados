#classe dos nós
class Node:  
  def __init__ (self, data):
    self.data = data
    self.next = None
    self.prev = None
 #classe para trabalhar com a lista em si    
class Lista_Duplamente_Encadeada:  
  def __init__(self):
    self.head = None
  def add(self, novo_node): #função usada para adicionar elementos na lista
        novo_node = Node(novo_node) #cria um novo nó
        if self.head: #caso o head não seja None
            node = self.head #guarda o valor da head
            self.head = novo_node  #transformar a head no novo nó
            self.head.next = node  #move a antiga head pro próximo
            self.head.next.prev = self.head  
            #coloca o antecessor do segundo elemento como o novo nó (já que é duplamente encadeada)
        else:
            self.head = novo_node  #caso o head seja nulo, isto é, a lista tá vazia, insere o primeiro elemento dela na head
  def rem(self, node):  #função de remoção de um nó
        if self.head.data == node:   #se o dado da head seja igual ao nó dado no input
            self.head = self.head.next #elimina a head o transformando no próximo elemento
            self.head.prev = None
        else: #caso a head não seja igual ao input
            antecessor = self.head  #se cria uma antecessor e um sucessor para realizar a comparação
            sucessor = self.head.next
            while sucessor: #enquanto o sucessor não é None
                if sucessor.data == node:  #caso o sucessor seja igual ao nó dado
                    antecessor.next = sucessor.next #o próximo elemento do antecessor vira no próximo elemento do sucessor
                    sucessor.next = antecessor.prev #e o próximo elemento 
                    sucessor = None
                else:
                    antecessor = sucessor 
                    sucessor = sucessor.next
  def exib(self, node): #função para exibir os dados dos nós
    node = self.head #começando o print da head
    while node: 
    #ele vai printando, enquanto percorre do início até o final, quando o valor for None e o while parar
        print(node.data),
        node.prev = node
        node = node.next
comando = ()
lista = Lista_Duplamente_Encadeada() #criando uma instância da Lista_Duplamente_Encadeada
counter = int()
while counter == 0: #while vai durar até que seja digitado um END e o contador some um
  comando = input().split(' ')
  if comando[0] != 'END':
    if comando[0] == 'ADD':
        lista.add(comando[1]) #chamando a função para inserir um nó
    elif comando[0] == 'REM':
        lista.rem(comando[1]) #chamando a função para remover um nó
    elif comando[0] == 'EXIB':
        lista.exib(lista.head) #chamando a função para exibir os dados de todos os nós na lista
    elif comando[0] == 'FIND': #comando para puxar um elemento para a head
           lista.rem(comando[1]) #remove o elemento de onde esteja e adiciona no início
           lista.add(comando[1])
  else:
    counter += 1  