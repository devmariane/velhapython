class JogoDaVelha:
  def __init__(self):
       self.tabuleiro = {
         '7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '
         }
       self.rodada = 1

  def exibirTabuleiro(self):
    print("┌───┬───┬───┐")
    print(f"│ {self.tabuleiro['7']} │ {self.tabuleiro['8']} │ {self.tabuleiro['9']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['4']} │ {self.tabuleiro['5']} │ {self.tabuleiro['6']} │")
    print("├───┼───┼───┤")
    print(f"│ {self.tabuleiro['1']} │ {self.tabuleiro['2']} │ {self.tabuleiro['3']} │")
    print("└───┴───┴───┘")
  
  def Rodada(self):
     while not self.Vencedor or not self.Velha():
        rodada += 1
        return rodada
     
  def ProximoJogador(self):
    if self.Rodada()%2==0:
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
      if self.tabuleiro['a'] and self.tabuleiro['b'] == self.tabuleiro['c']:
        return True
        
     
  def Velha(self):
    for i in self.tabuleiro:
      if i == ' ':
         return True