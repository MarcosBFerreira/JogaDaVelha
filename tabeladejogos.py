def tabela_de_jogos():

    print('=' * 40)
    print('             Tabela de Jogos')
    print('=' * 40)

    print('\n1 - Jogo da Velha\n')
    print('=' * 40)

    opcao = ''

    while opcao != '1':

        opcao = str(input('\nDigite o número do jogo: '))

        if opcao != '1':

            print('\nOpção Inválida!\nTente novamente!')

    print('\n')

    return opcao
