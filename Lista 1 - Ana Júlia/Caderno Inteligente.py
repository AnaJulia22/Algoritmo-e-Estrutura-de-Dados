vazio = False
try:
  capas = list(input())
except EOFError:   
  vazio = True
frente = []
verso = []
F = False
indice = True
counter = int()
if vazio == False:
    for i in range(len(capas)):
        if capas[i] == 'F':    #se o elemento na posição i for F, adiciona a posição a lista 'frente'
            frente.append(i)
    for a in range(len(capas)):
        if capas[a] == 'V':    #se o elemento na posição i for V, adiciona a posição a lista 'verso'
            verso.append(a)
if len(frente) == len(verso):  #se as listas tiverem tamanho igual, então checaremos se as posições estão certas
  for i in range(len(frente)):
        if verso[i] > frente[i]: #como o V tem que vir sempre depois do F, então cada posição de V terá que ser maior que a posição do f
           counter = counter     #exemplo: frente[1, 3, 5] e verso[2, 4, 6] o primeiro elemento de v tem que ser maior que o primeiro de frente, assim em diante...
        else:
           counter+=1     #caso uma posição de f seja maior que v, então o contador irá somar um
           posicao = verso[i] #salvando a posição que está errada para botar no print
  if counter > 0:
        posicao = posicao + 1
        print(f'Incorreto, devido a capa na posição {posicao}.')
  else:          #caso o contador se manter em 0, então todas as posições estão corretas
        print('Correto.') 
elif len(frente) > len(verso):  #caso tenha mais Fs que Vs
  b = len(verso)              #salvo o tamanho da lista de v para pegar o próximo f da lista frente e salvar a posição de onde está errado
  posicao = (frente[b] + 1)   #exemplo: frente[1, 3, 4,7], verso[2, 5, 6], len(verso) = 3, então b = 3+1 = 4(a posição do f errado)
  print(f'Incorreto, devido a capa na posição {posicao}.')
elif len(frente) < len(verso): #caso tenha mais Vs que Fs
  for i in range(len(frente)): 
        if verso[i] > frente[i]: #se a posição do v for maior que f, então está correto
           counter = counter
        else:                    #quando achar o v errado, isto é, com a posição menor que o f, o contador somará mais um
           counter+=1            #frente[1, 4, 5], verso[2, 3, 6, 7] quando vier um verso antes de sua frente
           posicao = verso[i]    #salvando a posição do V errado
  if counter > 0:
        posicao = posicao + 1
        print(f'Incorreto, devido a capa na posição {posicao}.')
  else:               #caso o contador não some nada, é porque é a mesma lógica da relação do tamanho da lista, o v errado será a posição de número um a mais do tamanho da lista frente
    b = len(frente) 
    posicao = (verso[b] + 1)
    print(f'Incorreto, devido a capa na posição {posicao}.')