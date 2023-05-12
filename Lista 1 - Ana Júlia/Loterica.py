class Node:     #class nó
    def __init__(self, data):
        self.data = data  #dado do nó
        self.next = None  #seu próximo  
        self.dinheiro = None #o dinheiro do nó (da pessoa)
class Fila:     #class da fila
  def __init__(self):
    self.primeiro = None 
    self.ultimo = None
    self._size = 0
  def __len__(self):
        return self._size   #quando eu usar len, retornará o size (tamanho)
  def add_N(self, N, dinheiro):   #função para adicionar as pessoas à fila
    node = Node(N)          #cria um novo nó
    if self.primeiro is None:     #se não tiver um primeiro elemento, então adiciona o novo nó como primeiro
      self.primeiro = node
      self.primeiro.dinheiro = dinheiro
    if self.ultimo:               #se existir um último elemento, adiciona o novo elemento após ele
      self.ultimo.next = node
      self.ultimo = node
      self.ultimo.dinheiro = dinheiro
    else:                         #caso não exista, então adiciona o nó como último
       self.ultimo = node
       self.ultimo.dinheiro = dinheiro
    self._size = self._size + 1   #atualiza o tamanho da fila
  def proximo(self):              #função para retirar o primeiro da fila quando ele for chamado para o caixa
    if self.primeiro:
      primeiro_fila = self.primeiro  #salva o primeiro da fila
      self.primeiro = self.primeiro.next  #coloca o seu próximo como primeiro
      if self._size == 1:
            self.ultimo = self.primeiro  #se apenas tiver um, o ultimo e o primeiro virará a mesma coisa
      return primeiro_fila  #retorna o antigo primeiro
  def proximo_fila1(self, caixa):    #função para a fila 1
      primeiro_da_fila1 = fila1.proximo()     #chama a função próximo que retorna quem é o primeiro da fila
      pessoa = primeiro_da_fila1.data     #guarda o dado do nó para o print
      dinheiro = float(primeiro_da_fila1.dinheiro) #transforma o dinheiro do susposto nó em float e o salva
      caixa = caixa + dinheiro     #adiciona ao caixa
      print(f'{pessoa} foi chamado para o caixa 1')
      self._size = self._size - 1  #atualiza o tamanho da fila
      return caixa  #retorna o valor da caixa atualizado
  def proximo_fila2(self, caixa):  #mesma lógica pra fila 2
          primeiro_da_fila2 = fila2.proximo()
          pessoa = primeiro_da_fila2.data
          dinheiro = float(primeiro_da_fila2.dinheiro)
          caixa = caixa + dinheiro
          print(f'{pessoa} foi chamado para o caixa 2')
          self._size = self._size - 1
          return caixa
  def move_metade2para1(self):  #função para mover a metade de uma fila para outra
        counter = int()
        metade = len(fila2)//2  #divide por dois, só que esse operador arredonda pro piso
        if (len(fila2)%2) != 0:  #então, se a divisão der um número decimal, somará um para arrendodá-lo para valor teto
                metade = metade + 1
        while counter != metade: #enquanto o contador não for igual a metade da fila, será adicionado o último elemento de uma fila para a outra fila
           counter+=1
           fila1.add_N(self.ultimo, self.ultimo.dinheiro)
           antecessor = self.primeiro
           sucessor = self.primeiro.next
           for i in range(self._size):
                if sucessor == self.ultimo: #caso o sucessor for igual ao último elemento, então o self.ultimo será igual ao antecessor, assim atualizando a fila
                   self.ultimo = antecessor
                else:
                   antecessor = sucessor #caso não seja, o antecessor vira o sucessor e o sucessor o próximo nó
                   sucessor = sucessor.next
        self._size = self._size - 1
  def move_metade1para2(self): #mesma lógica
        counter = int()
        metade = len(fila1)//2
        if (len(fila1)%2) != 0:
           metade = metade + 1
        while counter != metade:
           counter+=1
           fila2.add_N(self.ultimo.data, self.ultimo.dinheiro)
           antecessor = self.primeiro
           sucessor = self.primeiro.next
           for i in range(self._size):
                if sucessor == self.ultimo:
                   self.ultimo = antecessor
                else:
                   antecessor = sucessor
                   sucessor = sucessor.next
        self._size = self._size - 1
fila1 = Fila()
fila2 = Fila()
counter = int()
caixa_2 = int()
caixa_1 = int()
while counter == 0: #enquanto o contador for igual a 0, pedirá um input
  comando = input().split(' ')
  if comando[0] != 'FIM':  #caso o comando n seja igual a FIM
    if comando[0] == 'ENTROU:': #se for ENTROU, então será checado se é na fila 1 ou 2
      if comando[2] == '1':
        fila1.add_N(comando[1], comando[3]) #chama a função de adicionar nó, com os parâmetros de nome e dinheiro
        nome = comando[1]
        print(f'{nome} entrou na fila 1')
      elif comando[2] == '2':
        fila2.add_N(comando[1], comando[3])
        nome = comando[1]
        print(f'{nome} entrou na fila 2')
    elif comando[0] == 'PROXIMO:': #se for PROXIMO, será checado qual caixa está livre
      if comando[1] == '1':
        if fila1:  #se a fila 1 não estiver vazia, então será chamado a função de próximo
            caixa_1 = float(fila1.proximo_fila1(caixa_1))
        else: #caso esteja vazia, será chamado a função de mover metade e depois de próximo
           fila2.move_metade2para1()
           caixa_1 = float(fila1.proximo_fila1(caixa_1))
      elif comando[1] == '2':
        if fila2:
           caixa_2 = float(fila2.proximo_fila2(caixa_2))
        else:
           fila1.move_metade1para2()
           caixa_2 = float(fila2.proximo_fila2(caixa_2))
  else:
     counter+=1
else:
   print(f'Caixa 1: R$ {caixa_1:.2f}, Caixa 2: R$ {caixa_2:.2f}')