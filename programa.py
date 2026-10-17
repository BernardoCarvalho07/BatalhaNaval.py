from funcoes import *
import random 

embarcacoes = {
    "porta-aviões": [1, 4],
    "navio-tanque": [2, 3],
    "contratorpedeiro": [3, 2],
    "submarino": [4, 1]
}

frota = {}

# Posicionamento da frota: acontece uma única vez
for nome, informacoes in embarcacoes.items():
    quantidade = informacoes[0]
    tamanho = informacoes[1]

    for numero in range(quantidade):
        valida = False

        while not valida:
            print(
                f"Insira as informações referentes ao navio {nome} "
                f"que possui tamanho {tamanho}"
            )

            linha = int(input())
            coluna = int(input())

            if nome == "submarino":
                orientacao = "vertical"
            else:
                escolha = int(input())

                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"

            valida = posicao_valida(
                frota, linha, coluna, orientacao, tamanho
            )

            if not valida:
                print("Esta posição não está válida!")

        frota = preenche_frota(
            frota, nome, linha, coluna, orientacao, tamanho
        )

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro = posiciona_frota(frota)

jogando = True

while jogando:
    print(monta_tabuleiros(tabuleiro, tabuleiro_oponente))

    ja_atacado = True

    while ja_atacado:
        linha_valida = False
        coluna_valida = False

        while not linha_valida:
            linha = int(input())

            if 0 <= linha <= 9:
                linha_valida = True
            else:
                print("Linha inválida!")

        while not coluna_valida:
            coluna = int(input())

            if 0 <= coluna <= 9:
                coluna_valida = True
            else:
                print("Coluna inválida!")

        if tabuleiro_oponente[linha][coluna] not in ['X', '-']:
            ja_atacado = False

        else:
            print(
                f"A posição linha {linha} e coluna {coluna} "
                f"já foi informada anteriormente!"
            )

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False
    else:
        ja_atacado = True

        while ja_atacado:
            linha_oponente = random.randint(0, 9)
            coluna_oponente = random.randint(0, 9)

            if tabuleiro[linha_oponente][coluna_oponente] not in ['X', '-']:
                ja_atacado = False

        tabuleiro = faz_jogada( tabuleiro, linha_oponente, coluna_oponente)

        print(
            f"Seu oponente está atacando na linha {linha_oponente} "
            f"e coluna {coluna_oponente}"
        )

        if afundados(frota, tabuleiro) == 10:
            print("Xi! O oponente derrubou toda a sua frota =(")
            
            jogando = False


    

    
    