class Tree_Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
class Arvore_Busca_Binaria:
  def __init__(self):
    self.raiz = None
  def insercao(self, valor):  #função para inserir um novo valor
    node = Tree_Node(valor)
    if self.raiz is None:
      self.raiz = node 
    else:
      pai = None
      x = self.raiz
      while x:
        pai = x     #salva o nó folha para transformar em pai do valor inserido mais tarde
        if valor > x.data: #se valor maior que a raiz, 
          x = x.right     #então o x é atribuído como a raiz da subárvore a direita
        else:       #caso contrário, ele será atribuído a subárvore da esquerda
          x = x.left
      if valor > pai.data:  #se o valor a ser inserido for maior que o valor do pai, 
        pai.right = node #então o valor vai ser inserido a direita
      else:                 #caso contrário, será inserido a esquerda
        pai.left = node
    return node
  def Busca(self, valor, node = None):  #função de busca
    if self.raiz.data == valor:  #se a raiz for igual ao valor a ser encontrado, retorna a raiz
       return self.raiz
    if node is None:     
        node = self.raiz       #coloca node como o nó raiz para iniciar o processo de busca
    if node.left:          #se o nó tem filho a esquerda
       if node.left.data == valor:      #se o filho a esquerda for igual ao valor, retorna o filho a esquerda
            return node.left
       else:                           #caso não, chama a função de busca novamente. Agora a partir do nó a esquerda
            return self.Busca(valor, node.left)
    elif node.right:           #mesmo raciocínio
       if node.right.data == valor:
            return node.right
       else:
            return self.Busca(valor, node.right)
  def SCH(self, valor):        #função para mover o nó ao topo quando pesquisado
      x = self.Busca(valor)          
      pai = self.dad(x.data)
      while pai:              #enquanto o pai existir, ou seja, até que chegue a raiz da árvore total
         avo = self.dad(pai.data)
         if avo is None:         #se não tiver avô
              if x.data < pai.data:     #se o filho estiver a esquerda, a rotação será feita para a direita
                  self.move_right(pai)
              else:                     #se o filho estiver a direita, a rotação será feita para a esquerda
                  self.move_left(pai)
         else:                            #se tiver avô
              if avo.data < pai.data:     #se o pai tiver a direita do seu pai
                    if x.data > pai.data:  # e filho estiver a direita, rotaciona primerio o avô para a esquerda, depois o pai para a esquerda
                          self.move_left(avo)
                          self.move_left(pai)
                    else:                  # e filho estiver a esquerda, rotaciona primerio o pai para a direita, depois o avô para a esquerda
                          self.move_right(pai)
                          self.move_left(avo)
              else:                       #se o pai tiver a esquerda do seu pai
                    if x.data < pai.data:  # e filho estiver a esquerda, rotaciona primerio o pai para a direita, depois o avô para a direita
                          self.move_right(pai)
                          self.move_right(avo)
                    else:                  # e filho estiver a direita, rotaciona primerio o pai para a esquerda, depois o avô para a direita
                          self.move_left(pai)
                          self.move_right(avo)
         pai = x
         pai = self.dad(pai.data)
  def move_right(self, pai):     #rotação para direita
          filho = pai.left 
          pai.left = filho.right
          avo = self.dad(pai.data)
          if pai == self.raiz:
                self.raiz = filho
          elif pai.data > avo.data:
                avo.right = filho
          else:
                avo.left = filho
          filho.right = pai 
          
  def move_left(self, pai):      #rotação para esquerda
          filho = pai.right 
          pai.left = filho
          pai.right = filho.left
          avo = self.dad(pai.data)
          if pai == self.raiz:
                self.raiz = filho
          elif pai.data < avo.data:
                avo.left = filho
          else:
                avo.right = filho
          filho.left = pai
  def dad(self, valor):    #descobre o ascendente do nó
        y = self.raiz 
        pai = None
        while y.data != valor:
          pai = y    
          if valor > y.data: 
           y = y.right     
          else:       
           y = y.left
        return pai
  def _nivel(self, valor, nivel = 0):     #função para descobrir o nível do nó
    x = self.raiz
    while valor != x.data:
      if valor > x.data:
            x = x.right
      else:
            x = x.left
      nivel +=1
    return nivel
tree = Arvore_Busca_Binaria()  
try:
 while True:
  comando = input().split(' ')
  if comando[0] == 'ADD':
   tree.insercao(int(comando[1]))
   cl = tree._nivel(int(comando[1]))
   print(f'{cl}')
  elif comando [0] == 'SCH':
   buscando = tree.Busca(int(comando[1]))
   if buscando != None:
    pl = tree._nivel(int(comando[1]))
    tree.SCH(int(comando[1]))
   else:
    pl = (-1)
   print(f'{pl}')
except EOFError:
   pass