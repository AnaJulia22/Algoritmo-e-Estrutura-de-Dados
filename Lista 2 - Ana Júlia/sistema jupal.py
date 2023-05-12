class Tree_Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None
    self.altura = 1
class AVL_Tree:
  def __init__(self):
    self.raiz = None

  def inserir(self, nome):
    if self.raiz is None:   #caso a árvore esteja vazia, cria uma raiz
      self.raiz = Tree_Node(nome)
      verificacao = ('inserido')
      return verificacao
    else:
      x = self.raiz         #caso contrário, checaremos se o nome já existe na ávore
      pai = None
      while x.data != nome: 
        pai = x
        if x.data > nome:
          x = x.left
        else:
          x = x.right
        if x == None or x == 0: 
            break
      if x is None or x == 0:  #caso não exista, será criado um novo nó 
            novo_node = Tree_Node(nome)
            if pai.data > novo_node.data:   #se o valor do nó for menor que o do seu pai, ele será inserido a esquerda do pai
               pai.left = novo_node
            else:                            #se for maior, será inserido a direita
               pai.right = novo_node
            verificacao = ('inserido')
            pai.altura = 1 + max(self.Altura(pai.right), self.Altura(pai.left)) #atualizando a altura do pai
            if pai != self.raiz:         #se o pai não for a raiz
               y = pai
               while y != self.raiz:                    
                    fb = self.FatorBalanceamento(y) #verifica o fator de balanceamento do pai, se não estiver estável, passará pelo processo de balanceamento
                    if fb > (1):
                        if self.FatorBalanceamento(y.left) >= 0:
                            self.move_esquerda(y)
                            break
                        else:
                            y.left = self.move_direita(y.left)
                            self.move_esquerda(y)
                            break
                    elif fb < (-1):
                        if self.FatorBalanceamento(y.right) <= 0:
                            self.move_direita(y)
                            break
                        else:
                            y.right = self.move_esquerda(y.right)
                            self.move_direita(y)
                            break
                    else:                          #se estiver estável, verificaremos o fb do avô
                        y = self.dad(y.data)
                        y.altura = 1 + max(self.Altura(y.right), self.Altura(y.left))
               else:       #se chegamos na raiz, é verificado seu fb
                    y.altura = 1 + max(self.Altura(y.right), self.Altura(y.left))
                    self.Balanco(y)  #faz o balanço uma última vez na raiz
            return verificacao
      else:  
        verificacao = ('ja existe')
        return verificacao
    
  def Balanco(self, pai):
    fb = self.FatorBalanceamento(pai)
    if fb > (1):   #se o fb for maior que 1, quer dizer que a árvore está instável para a esquerda, então a rotação será realizada para a direita
        if self.FatorBalanceamento(pai.left) >= 0:
            self.move_esquerda(pai)
        else:
            pai.left = self.move_direita(pai.left)
            self.move_esquerda(pai)
    elif fb < (-1):    #se o fb for menor que -1, quer dizer que a árvore está instável para a direita, então a rotação será realizada para a esquerda
        if self.FatorBalanceamento(pai.right) <= 0:
            self.move_direita(pai) 
        else:
            pai.right = self.move_esquerda(pai.right)
            self.move_direita(pai)

  def move_esquerda(self, pai):
        y = pai.right   
        avo = self.dad(pai.data)     
        if y.left:                 #se o filho do pai tem filho a esquerda
              if pai is self.raiz: #se o pai é a raiz
                  self.raiz = y.left  #substitui a raiz pelo filho a esquerda para ficar em ordem
                  novo_pai = self.raiz
              else:
                  novo_pai = y.left
              y.left= None        #remove o filho do filho do pai
              novo_pai.left = pai   #coloca como filho da raiz a esquerda o avô do novo pai
              novo_pai.right = y    #coloca como filho da raiz a direita o pai do novo pai
              pai.right = y.left
              if avo:                   #se o pai antigo tem avô, liga o avô ao novo pai
                if pai.data < avo.data:  
                  avo.left = novo_pai
                else:                    
                  avo.right = novo_pai 
        else:                  #se o filho do pai não tem filho a esquerda
          pai.right = y.left   #coloca com o filho direito do pai, o filho esquerdo do filho            
          if pai is self.raiz: #se o pai é raiz
            self.raiz = y       #então coloca o filho como raiz
          else:                #caso contrário, descobre o avô
           avo = self.dad(pai.data)    
           if pai.data < avo.data:  #se o pai é menor que o avô, coloca a esquerda do avô o seu neto
                avo.left = y
           else:                    #se o pai é maior que o avô, coloca a direita do avô o seu neto
                avo.right = y    
          y.left = pai      #coloca o pai como filho 
        pai.altura = 1 + max(self.Altura(pai.left), self.Altura(pai.right))  #atualiza as alturas
        y.altura = 1 + max(self.Altura(y.left), self.Altura(y.right))

  def move_direita(self, pai):     #mesmo raciocínio
        y = pai.left  
        avo = self.dad(pai.data)      
        if y.right:
          if pai is self.raiz:
               self.raiz = y.right
               novo_pai = self.raiz
          else:
               novo_pai = y.right          
          y.right = None
          novo_pai.left = y
          novo_pai.right = pai
          pai.left = y.right          
          if avo:
            if pai.data < avo.data:
                avo.left = novo_pai
            else:
                avo.right = novo_pai  
        else:
          pai.left = y.right             
          avo = self.dad(pai.data)
          if pai is self.raiz:
            self.raiz = y
          else:
            if pai.data < avo.data:
                avo.left = y
            else:
                avo.right = y    
          y.right = pai    
        pai.altura = 1 + max(self.Altura(pai.left), self.Altura(pai.right)) 
        y.altura = 1 + max(self.Altura(y.left), self.Altura(y.right)) 

  def dad(self, valor):        #descobrir o ascendente do nó
        x = self.raiz
        pai = None
        while x.data != valor: 
          pai = x   
          if valor > x.data: 
           x = x.right     
          else:       
           x = x.left
        return pai
  
  def Altura(self, node = 0):     #função para pegar a altura de um nó específico
        if node == None:
              return 0
        if node == 0:
              node = self.raiz
              if self.raiz == None:
                return 0
              else:
                return node.altura
        else:
          return node.altura
  def nivel(self):
        contador = int()
        if self.raiz:
          node = self.raiz
          fb = self.FatorBalanceamento(node)
          while node != None:
            if fb == 0:
              if node.right:
                node = node.right
                contador +=1
              elif node.left:
                node = node.left
                contador +=1
              else:
                    contador+=1
                    break
            elif fb == 1:
              if node.right:
                node = node.right
                contador +=1
              elif node.left:
                node = node.left
                contador+=1
              else:
                    contador+=1
                    break
            else:
              if node.left:            
                node = node.left
                contador +=1
              elif node.right:
                node = node.right
                contador +=1
              else:
                    contador += 1
                    break
          return contador
        else:
              return None              
        
  def FatorBalanceamento(self, root):      #função para descobri o fator de balanceamento de uma raiz
        if not root:
            return 0
        return (self.Altura(root.right) - self.Altura(root.left)) 
   
  def max(self, node = 0):      #descobre o maior valor da árvore
      if node == 0:
        node = self.raiz
      if self.raiz:
       while node.right:
          node = node.right
       return node.data
      else:
            return None
      
  def min(self, node = 0):    #descobre o menor valor da árvore
      if node == 0:
        node = self.raiz
      if self.raiz:
       while node.left:
          node = node.left
       return node.data
      else:
          return None
      
  def EncaminhamentoEmOrdem(self, node = None):    #função para printar os nomes das árvores em ordem alfabética
        ultimo = self.max()
        if node == None:
              node = self.raiz
        if self.raiz:
              if node.left:
                    self.EncaminhamentoEmOrdem(node.left)
              if node.data == ultimo:
                    print(node.data, end='')
              else:
                print(node.data, end=' ')
              if node.right:
                    self.EncaminhamentoEmOrdem(node.right)

        else:
            return print('ARVORE VAZIA')

  def Deletar(self, nome, node = 0):
    if node == 0:
          node = self.raiz
    if node == None: #caso não ache o nome, retorna 0
          return print(f'{nome} NAO ENCONTRADO')
    elif nome < node.data:  #se o valor do nome ainda n foi encontrado e for menor que o nó atual, faz a recursão agora com o nome da esquerda
        node.left = self.Deletar(nome, node.left)
    elif nome > node.data:  #se o valor do nome ainda n foi encontrado e for maior que o nó atual, faz a recursão agora com o nome da direita
        node.right = self.Deletar(nome, node.right)
    else:                   #quer dizer que achou o nome
        if node.right == None and node.left == None:     #se não tiver nenhum filho
                if node == self.raiz:     
                      self.raiz = None          #se for a raiz, remove a raiz
                      print(f'{comando[1]} DELETADO')
                      return self.raiz                  
                else:
                  print(f'{comando[1]} DELETADO')
                  return None                #se não for a raiz, só remove o nó
        elif node.right == None:      #se não tiver filho a direita
            if node == self.raiz:      #se for a raiz e tiver filho a esquerda, então substitui a raiz pelo seu filho
              self.raiz = node.left
              print(f'{comando[1]} DELETADO')
              return self.raiz
            else:
              print(f'{comando[1]} DELETADO')
              return node.left
        elif node.left == None:     #se não tiver filho a esquerda
            if node == self.raiz:
              self.raiz = node.right   #se for a raiz e tiver filho a direita, então substitui a raiz pelo seu filho
              print(f'{comando[1]} DELETADO')
              return self.raiz
            else:
              print(f'{comando[1]} DELETADO')
              return node.right
        else:                          #se tiver filho dos dois lados,  
            fb = self.height(node.right) - self.height(node.left)
            if fb == -1 or fb == 0:      #se tiver mais nós no lado esquerdo ou se o fb estiver estável, substitui pelo menor filho do lado esquerdo, seu sucessor
              substituto = self.max(node.left)
              node.data = substituto
              node.left = self.Deletar(substituto, node.left) 
            else:                        #se tiver mais nós no lado direitro, substitui pelo menor filho do lado direito, seu sucessor
              substituto = self.min(node.right)
              node.data = substituto
              node.right = self.Deletar(substituto, node.right) #remove seu sucessor de lá de baixo   
    return node
  def height(self, node=None):
        if node is None:
            node = self.raiz
        hesquerda = 0
        hdireita = 0
        if node.left:
            hesquerda = self.height(node.left)
        if node.right:
            hdireita = self.height(node.right)
        if hdireita > hesquerda:
            return hdireita + 1
        return hesquerda + 1
    
arvore = AVL_Tree()
counter = int()
while counter == 0:
  comando = input().split(' ')
  if comando[0] == ('INSERIR'):
    verificacao = arvore.inserir(comando[1])
    if verificacao == ('inserido'):
          print(f'{comando[1]} INSERIDO')
    elif verificacao == ('ja existe'):
          print(f'{comando[1]} JA EXISTE')
  elif comando[0] == ('DELETAR'):
    verificacao = arvore.Deletar(comando[1])
  elif comando[0] == ('MINIMO'):
    verificacao = arvore.min()
    if verificacao:
          print(f'MENOR: {verificacao}')
    else:
          print('ARVORE VAZIA')
  elif comando[0] == ('MAXIMO'):
    verificacao = arvore.max()
    if verificacao:
          print(f'MAIOR: {verificacao}')
    else:
          print('ARVORE VAZIA')
  elif comando[0] == ('ALTURA'):
    altura = arvore.nivel()
    print(f'ALTURA: {altura}')
  elif comando[0] == ('FIM'):
     counter+=1
else:
       arvore.EncaminhamentoEmOrdem()