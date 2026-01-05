from peca import Peca

class Bispo(Peca):
    def movimentos_possiveis(self, x, y, tabuleiro):
        moves = []

        direcoes = [(1,1), (1,-1), (-1,1), (-1,-1)]

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                p = tabuleiro.obter_peca(nx, ny)
                if p is None:
                    moves.append((nx, ny))
                elif p.cor != self.cor:
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy

        return moves
