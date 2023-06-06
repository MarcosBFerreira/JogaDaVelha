import jogo_da_velha.tabuleiro as tabu
import os
import random


def jogada_jogador(jogada, validade, contador, tabuleiro, jogador1, escolha_jogador1, modo_jogo):

    if contador <= 8:
                
        while validade is not True:
                    
            print(f'\nVez do(a) jogador(a) {jogador1}')
            if modo_jogo == 2:

                if contador > 0:
                    if contador % 2 == 0:
                        aleatorio = str(random.randint(1, 9))
                        print('Posição: ' + aleatorio)
                        jogada.append(aleatorio)

                    else:
                        jogada.append(str(input('Posição: ')))

                else:

                    print('Posição: 5')
                    jogada.append('5')
            else:
                jogada.append(str(input('Posição: ')))

            match jogada[-1]:

                case '1':
                    if tabuleiro[0][0] == '1':
                        tabuleiro[0][0] = escolha_jogador1
                        validade = True
                        break

                case '2':
                    if tabuleiro[0][1] == '2':
                        tabuleiro[0][1] = escolha_jogador1
                        validade = True
                        break
                        
                case '3':
                    if tabuleiro[0][2] == '3':
                        tabuleiro[0][2] = escolha_jogador1
                        validade = True
                        break
                        
                case '4':
                    if tabuleiro[1][0] == '4':
                        tabuleiro[1][0] = escolha_jogador1
                        validade = True
                        break
                        
                case '5':
                    if tabuleiro[1][1] == '5':
                        tabuleiro[1][1] = escolha_jogador1
                        validade = True
                        break

                case '6':
                    if tabuleiro[1][2] == '6':
                        tabuleiro[1][2] = escolha_jogador1
                        validade = True
                        break
                        
                case '7':
                    if tabuleiro[2][0] == '7':
                        tabuleiro[2][0] = escolha_jogador1
                        validade = True
                        break
                        
                case '8':
                    if tabuleiro[2][1] == '8':
                        tabuleiro[2][1] = escolha_jogador1
                        validade = True
                        break
                        
                case '9':
                    if tabuleiro[2][2] == '9':
                        tabuleiro[2][2] = escolha_jogador1
                        validade = True
                        break
                    
            if validade is False:
                print('Jogada inválida!\nJogue novamente!')
        os.system('cls' if os.name == 'nt' else 'clear') or None
        tabu.tabuleiro_partida(tabuleiro)

    return jogada, validade, tabuleiro
