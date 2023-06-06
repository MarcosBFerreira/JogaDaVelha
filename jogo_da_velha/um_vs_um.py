import os
import jogo_da_velha.tabuleiro as tabu
import jogo_da_velha.cadastrar as cadas
import jogo_da_velha.placar_jogo_da_velha as placar
import jogo_da_velha.validação_jogo_da_velha as validacao
import jogo_da_velha.jogadas as jogadas


def um_vs_um():
    
    vencedor = ''
    jogada = []
    contador = 0
    validade = False
    placar_jogador1 = 0
    placar_jogador2 = 0
    continuar = ''
    jogador1, jogador2, escolha_jogador1, escolha_jogador2 = cadas.cadastrar()

    os.system('cls' if os.name == 'nt' else 'clear') or None

    tabuleiro = tabu.tabuleiro()
    
    while continuar != '2':

        continuar = 0

        while contador <= 8:

            jogada, validade, tabuleiro = jogadas.jogada_jogador(jogada, validade, contador, tabuleiro, jogador1,
                                                                 escolha_jogador1, 1)

            validade = False
            contador += 1

            vencedor, placar_jogador1 = validacao.validacao(tabuleiro, vencedor, escolha_jogador1, jogador1,
                                                            placar_jogador1)
            vencedor, placar_jogador2 = validacao.validacao(tabuleiro, vencedor, escolha_jogador2, jogador2,
                                                            placar_jogador2)

            if vencedor != '':
                break

            jogada, validade, tabuleiro = jogadas.jogada_jogador(jogada, validade, contador, tabuleiro, jogador2,
                                                                 escolha_jogador2, 1)

            contador += 1
            validade = False

            vencedor, placar_jogador1 = validacao.validacao(tabuleiro, vencedor, escolha_jogador1, jogador1,
                                                            placar_jogador1)
            vencedor, placar_jogador2 = validacao.validacao(tabuleiro, vencedor, escolha_jogador2, jogador2,
                                                            placar_jogador2)

            if vencedor != '':
                break
            
        if vencedor == '':
            print('\nNinguém venceu! Deu Velha!\n')
        
        placar.placar_jogo_da_velha(jogador1, placar_jogador1, jogador2, placar_jogador2)
        
        while continuar != '1' and continuar != '2':
            continuar = str(input('\nDeseja continuar?\n1 - Sim  2 - Não\n\n: '))
            if continuar != '1' and continuar != '2':
                print('\nNúnero inválido!')
        
        if continuar == '1':
            
            tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0
            vencedor = ''
            os.system('cls' if os.name == 'nt' else 'clear') or None

        if continuar != '2':
            tabu.tabuleiro_partida(tabuleiro)

    print('\nMuito obrigado por jogar!\n')
