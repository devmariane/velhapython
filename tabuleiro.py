class JogoDaVelha:
  def __init__(self):
       self.tabuleiro = {
         7: ' ', 8: ' ', 9: ' ',
         4: ' ', 5: ' ', 6: ' ',
         1: ' ', 2: ' ', 3: ' '
         }
       self.rodada = 0

  def getRodada(self):
    return self.rodada

  def setRodada(self, numeroRodada):
    self.rodada = numeroRodada

  def ExibirTabuleiro(self):
    print("┌───┬───┬───┐")
    print(f"│ {self.tabuleiro[7]} │ {self.tabuleiro[8]} │ {self.tabuleiro[9]} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro[4]} │ {self.tabuleiro[5]} │ {self.tabuleiro[6]} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro[1]} │ {self.tabuleiro[2]} │ {self.tabuleiro[3]} │")
    print("└───┴───┴───┘")
  
  def IniciarJogo(self):
     jogardnv = True
     while jogardnv:
      while not self.Vencedor() and not self.Velha():
          self.ExibirTabuleiro()
          posicao = int(input(f"Vez de {self.ProximoJogador()}: "))
          self.ValidarPosicao(posicao)

      if self.Velha():
        self.ExibirTabuleiro()
        print("fim de jogo: deu velha!")
        novojogo = input("Jogar novamente?(S/N)")
        if novojogo == 'N' or novojogo == 'n':
          jogardnv = False
      else:
        self.ExibirTabuleiro()
        vencedor = self.ProximoJogador()
        print(f"Fim de jogo vencedor: {vencedor}")
        novojogo = input("Jogar novamente?(S/N)")
        if novojogo == 'N' or novojogo == 'n':
          jogardnv = False
  
  def ProximoJogador(self):
    rodada = self.getRodada()
    if rodada%2==0:
      return "x"
    else:
      return "O"
  def Vencedor(self):
    lines = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
    [7, 5, 3],
    [1, 5, 9],
    ]
    for i, (a, b, c) in enumerate(lines):
      if self.tabuleiro[a] == self.tabuleiro[b] and self.tabuleiro[b] == self.tabuleiro[c] and self.tabuleiro[a] != ' ':
        return True
    return False
  def Velha(self):
    for chave in sorted(self.tabuleiro):
      if self.tabuleiro[chave] == ' ':
         return False

  def ValidarPosicao(self, posicao):
    rodada = self.getRodada()
    if self.tabuleiro[posicao] == ' ':
      valorJogador = self.ProximoJogador()
      self.tabuleiro[posicao] = valorJogador
      self.setRodada(rodada+1)
    else:
      print("Posicao invalida, jogue novamente")