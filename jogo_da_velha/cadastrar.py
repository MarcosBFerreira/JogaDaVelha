def cadastrar():

    print('=' * 40)
    print('     Bem-vindos ao Jogo da Velha')
    print('=' * 40)
    print('           Tela de cadastro')
    print('=' * 40)
    jogador1 = str(input('\nDigite o nome do Jogador 1: '))
    jogador2 = str(input('Digite o nome do Jogador 2: '))
    escolha_jogador1 = ''

    while escolha_jogador1 != 'X' and escolha_jogador1 != 'O':
        escolha_jogador1 = str(input(f'\n{jogador1} escolha entre X ou O: ')).upper()

        if escolha_jogador1 != 'X' and escolha_jogador1 != 'O':
            print('\nEscolha inválida!\n')

    if escolha_jogador1 == 'X':

        escolha_jogador2 = 'O'

    else:

        escolha_jogador2 = 'X'

    return jogador1, jogador2, escolha_jogador1, escolha_jogador2
