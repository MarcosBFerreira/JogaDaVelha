def validacao_jogador(tabuleiro, vencedor, escolha_jogador1, jogador1, placar_jogador1):

    primeira_casa = tabuleiro[0][0] == escolha_jogador1
    segunda_casa = tabuleiro[0][1] == escolha_jogador1
    terceira_casa = tabuleiro[0][2] == escolha_jogador1
    quarta_casa = tabuleiro[1][0] == escolha_jogador1
    quinta_casa = tabuleiro[1][1] == escolha_jogador1
    sexta_casa = tabuleiro[1][2] == escolha_jogador1
    setima_casa = tabuleiro[2][0] == escolha_jogador1
    oitava_casa = tabuleiro[2][1] == escolha_jogador1
    nona_casa = tabuleiro[2][2] == escolha_jogador1

    primeira_horizontal = primeira_casa and segunda_casa and terceira_casa
    segunda_horizontal = quarta_casa and quinta_casa and sexta_casa
    terceira_horizontal = setima_casa and oitava_casa and nona_casa
    primeira_diagonal = primeira_casa and quinta_casa and nona_casa
    segunda_diagonal = terceira_casa and quinta_casa and setima_casa
    primeira_vertical = primeira_casa and quarta_casa and setima_casa
    segunda_vertical = segunda_casa and quinta_casa and oitava_casa
    terceira_vertical = terceira_casa and sexta_casa and nona_casa

    if primeira_horizontal:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1
        
    elif segunda_horizontal:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    elif terceira_horizontal:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    elif primeira_diagonal:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    elif segunda_diagonal:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    elif primeira_vertical:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    elif segunda_vertical:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    elif terceira_vertical:
        print(f'\n{jogador1} venceu! Parabéns\n')
        vencedor = jogador1
        placar_jogador1 += 1

    return vencedor, placar_jogador1


def validacao(tabuleiro, vencedor, escolha_jogador1, jogador1, placar_jogador1):

    tabu = tabuleiro
    vence = vencedor
    
    escolha_jgd1 = escolha_jogador1
    jgd1 = jogador1
    placar_jgd1 = placar_jogador1

    vence, placar_jgd1 = validacao_jogador(tabu, vence, escolha_jgd1, jgd1, placar_jgd1)

    return vence, placar_jgd1
