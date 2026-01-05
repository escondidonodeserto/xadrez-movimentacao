from peca import Peca

class Peao(Peca):
    def movimentos_possiveis(self, x, y, tabuleiro):
        moves = []
        direcao = -1 if self.cor == "branca" else 1

        # Movimento simples
        if tabuleiro.obter_peca(x, y+direcao) is None:
            moves.append((x, y+direcao))

        # Movimento duplo na saída
        if (self.cor == "branca" and y == 6) or (self.cor == "preta" and y == 1):
            if tabuleiro.obter_peca(x, y+direcao) is None and tabuleiro.obter_peca(x, y+2*direcao) is None:
                moves.append((x, y+2*direcao))

        # Capturas diagonais
        for dx in (-1, 1):
            nx = x + dx
            ny = y + direcao
            p = tabuleiro.obter_peca(nx, ny)
            if p and p.cor != self.cor:
                moves.append((nx, ny))

        return moves
