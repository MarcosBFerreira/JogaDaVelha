def tabuleiro():

    print('=' * 40)
    print('                Tabuleiro')
    print('=' * 40)

    print('\n')
    
    tabuleiro = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    print(f"""        {tabuleiro[0][0]}   |   {tabuleiro[0][1]}   |   {tabuleiro[0][2]}
        ------------------
        {tabuleiro[1][0]}   |   {tabuleiro[1][1]}   |   {tabuleiro[1][2]}
        ------------------
        {tabuleiro[2][0]}   |   {tabuleiro[2][1]}   |   {tabuleiro[2][2]}""")
    
    print('\n')
    print('=' * 40)

    return tabuleiro


def tabuleiro_partida(tabuleiro):
    print('=' * 40)
    print('                Tabuleiro')
    print('=' * 40)

    tabu = print(f'''\n        {tabuleiro[0][0]}   |   {tabuleiro[0][1]}   |   {tabuleiro[0][2]}
        ------------------
        {tabuleiro[1][0]}   |   {tabuleiro[1][1]}   |   {tabuleiro[1][2]}
        ------------------
        {tabuleiro[2][0]}   |   {tabuleiro[2][1]}   |   {tabuleiro[2][2]}''')

    print('\n')
    print('=' * 40)

    return tabu
