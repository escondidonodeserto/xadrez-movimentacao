from peca import Peca
from torre import Torre
from bispo import Bispo

class Rainha(Peca):
    def movimentos_possiveis(self, x, y, tabuleiro):
        return Torre.movimentos_possiveis(self, x, y, tabuleiro) + \
               Bispo.movimentos_possiveis(self, x, y, tabuleiro)
