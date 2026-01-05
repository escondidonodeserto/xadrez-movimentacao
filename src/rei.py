from peca import Peca

class Rei(Peca):
    def movimentos_possiveis(self, x, y, tabuleiro):
        moves = []
        offsets = [
            (1,0), (-1,0), (0,1), (0,-1),
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]

        for dx, dy in offsets:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if tabuleiro.posicao_livre_ou_inimigo(nx, ny, self.cor):
                    moves.append((nx, ny))

        return moves
