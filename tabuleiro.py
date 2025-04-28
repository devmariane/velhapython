class JogoDaVelha:
  def __init__(self):
       self.tabuleiro = {
         '7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '
         }

  def ExibirTabuleiro(self):
    print("┌───┬───┬───┐")
    print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
    print("└───┴───┴───┘")
  
  def IniciarJogo(self):
     jogardnv = True
     while jogardnv:
      while not self.Vencedor() or not self.Velha():
          rodada = 0
          self.ExibirTabuleiro()
          
          posicao = input(f"Vez de {self.ProximoJogador(rodada)}: ")
          self.ValidarPosicao(posicao, rodada)
          return rodada
      if self.Velha():
        print("fim de jogo: deu velha!")
        novojogo = input("Jogar novamente?(S/N)")
        if novojogo == 'N' or novojogo == 'n':
          jogardnv = False
      else:
        print(f"Fim de jogo vencedor: {self.ProximoJogador}")
        novojogo = input("Jogar novamente?(S/N)")
        if novojogo == 'N' or novojogo == 'n':
          jogardnv = False
  
  def ProximoJogador(self, rodada):
    if rodada%2==0:
      return "x"
    else:
      return "O"
  def Vencedor(self):
    print("Chama Vencedor")
    lines = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    ['7', '4', '1'],
    ['8', '5', '2'],
    ['9', '6', '3'],
    ['7', '5', '3'],
    ['1', '5', '9'],
    ]
    for i, (a, b, c) in enumerate(lines):
      if self.tabuleiro[a] and self.tabuleiro[b] == self.tabuleiro[c]:
        return True
     
  def Velha(self):
    print("Chama Velha")
    for i in self.tabuleiro:
      if i == ' ':
         return True

  def ValidarPosicao(self, posicao, rodada):
    if self.tabuleiro[posicao] == ' ':
      self.tabuleiro[posicao] == self.ProximoJogador
      rodada += 1
    else:
      print("Posicao invalida, jogue novamente")