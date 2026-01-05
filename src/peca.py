class Peca:
    def __init__(self, cor):
        self.cor = cor  # "branca" ou "preta"

    def movimentos_possiveis(self, x, y, tabuleiro):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")