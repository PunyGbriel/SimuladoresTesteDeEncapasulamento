class Cliente:
    def __init__(self, n, f, e):

        self._nome = n
        self._telefone = f
        self._email = e
        self._saldo = 0

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
