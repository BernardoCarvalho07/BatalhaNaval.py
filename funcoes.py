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

