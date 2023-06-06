import os
from jogo_da_velha.um_vs_um import um_vs_um
from jogo_da_velha.um_vs_computador import um_vs_computador


def tipo_jogo_velha():

    print('=' * 40)
    print(' ' * 10 + 'Modalidade de Jogo')
    print('=' * 40)
    print('\n1 - 1 VS 1\n2 - 1 VS Computador\n')
    print('=' * 40)
    opcao = ''

    while opcao != '1' and opcao != '2':

        opcao = str(input('\nModalidade: '))

        if opcao != '1' and opcao != '2':

            print('\nOpção Inválida!\nTente novamente!')

    match opcao:

        case '1':

            os.system('cls' if os.name == 'nt' else 'clear') or None

            um_vs_um()

        case '2':

            os.system('cls' if os.name == 'nt' else 'clear') or None

            um_vs_computador()
