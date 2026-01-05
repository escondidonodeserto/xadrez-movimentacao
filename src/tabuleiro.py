class Tabuleiro:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]

    def colocar_peca(self, peca, x, y):
        self.grid[y][x] = peca

    def obter_peca(self, x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return self.grid[y][x]
        return None

    def posicao_livre_ou_inimigo(self, x, y, cor):
        p = self.obter_peca(x, y)
        return p is None or p.cor != cor
