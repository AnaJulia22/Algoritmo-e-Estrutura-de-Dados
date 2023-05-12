def torcida_foto():
    if n <= 2:
        return max(torcidas)
    M = [[0 for j in range(3)] for i in range(n)] #cria uma matriz com 3 colunas e n linhas
    M[1][0], M[1][1], M[1][2] = int(torcidas[1]), int(torcidas[0]), int(torcidas[2])
    for i in range(2, n): 
        #pega o máximo entre a soma número da posiçaõ i + o de duas casas antes dele e o número anterior a i
        M[i][0] = max(M[i-1][1] + int(torcidas[i]), M[i-1][0]) 
        #o máximo entre o primeiro e o segundo elemento da lista anterior
        M[i][1] = max(M[i-1][0], M[i-1][1])
        #next = próximo número da lista dada
        #[10, 5, 9], a próxima lista fica: [14, 10, next]
        if i < n-1:
            M[i][2] = int(torcidas[i+1])
    return max(M[n-1][0], M[n-1][1]) #retorna o maior número entre o primeiro e segundo elemento da última linha

n = int(input())
torcidas = input().split()
maior_soma = torcida_foto()
print(f'{maior_soma} torcedores podem ser fotografados.')