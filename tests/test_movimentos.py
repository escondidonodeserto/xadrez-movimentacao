from tabuleiro import Tabuleiro
from torre import Torre

def test_torre_movimento_livre():
    t = Tabuleiro()
    torre = Torre("branca")
    t.colocar_peca(torre, 0, 7)

    moves = torre.movimentos_possiveis(0,7,t)

    assert len(moves) > 0
