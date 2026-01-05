from peca import Peca

class Cavalo(Peca):
    def movimentos_possiveis(self, x, y, tabuleiro):
        moves = []
        offsets = [
            (2,1), (2,-1), (-2,1), (-2,-1),
            (1,2), (1,-2), (-1,2), (-1,-2)
        ]

        for dx, dy in offsets:
            nx, ny = x+dx, y+dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if tabuleiro.posicao_livre_ou_inimigo(nx, ny, self.cor):
                    moves.append((nx, ny))

        return moves
