def define_posicoes(linha,coluna,orientacao,tamanho):

    posicoes = []

    if orientacao == 'horizontal':

        for i in range(tamanho):
            posicoes.append([linha, coluna + i])

    if orientacao == 'vertical':

        for i in range(tamanho):
            posicoes.append([linha + i, coluna])

    return posicoes

def preenche_frota(frota, nome_do_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_do_navio in frota:
        frota[nome_do_navio].append(posicoes)
    else:
        frota[nome_do_navio] = [posicoes]

    return frota

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna]= 'X'
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro

def posiciona_frota(frota):
    tabuleiro = [[0] * 10 for i in range(10)]

    for tiposnavio, navios in frota.items():
        for navio in navios:
            for cordenadas in navio:
                tabuleiro[cordenadas[0]][cordenadas[1]] = 1

    return tabuleiro

def afundados(frota, tabuleiro):
    quantidade = 0

    for tiposnavio, navios in frota.items():
        for navio in navios:
            afundado = True

            for cordenadas in navio:
                if tabuleiro[cordenadas[0]][cordenadas[1]] != 'X':
                    afundado = False
                    break

            if afundado:
                quantidade += 1

    return quantidade
                
