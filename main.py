from tabuleiro import JogoDaVelha
jogo = JogoDaVelha()

jogo.exibirTabuleiro()
posicao = input(f"Vez de {jogo.ProximoJogador()}: ")
