from jogo_da_velha.tipo_jogo_velha import tipo_jogo_velha
import tabeladejogos
import os

os.system('cls' if os.name == 'nt' else 'clear') or None
opcao = tabeladejogos.tabela_de_jogos()

match opcao:
    case '1':
        os.system('cls' if os.name == 'nt' else 'clear') or None
        tipo_jogo_velha()
