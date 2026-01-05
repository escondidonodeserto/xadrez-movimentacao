from tabuleiro import Tabuleiro
from torre import Torre
from cavalo import Cavalo
from bispo import Bispo
from rainha import Rainha
from rei import Rei
from peao import Peao

def main():
    t = Tabuleiro()

    t.colocar_peca(Torre("branca"), 0, 7)
    t.colocar_peca(Rei("preta"), 4, 0)

    torre = t.obter_peca(0,7)
    print("Movimentos possíveis da torre branca:", torre.movimentos_possiveis(0,7,t))

if __name__ == "__main__":
    main()
