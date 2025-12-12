class televisor:
    def __init__(self, fabri, mode):
        self.fabri = fabri
        self.mode = mode
        self.canalatual = None
        self.list = []
        self.vol = 0

    def aumentaVolume(self, valor):
        if self.vol + valor <= 100:
            self.vol += valor
            print(f'Volume aumentado para {valor}')
        else:
            self.vol = 100
            print(f'Volume esta no maximo')

    def diminuirvolume(self,valor):
        if self.vol - valor >= 0:
            self.vol -= valor
            print(f'Volume foi diminuido para {self.vol}')
        else:
            self.vol = 0
            print(f'Volume esta em {self.vol} MUDO')

    def trocardecanal(self,valor):
        if valor in self.list:
            self.canalatual = valor
            print(f'O canal atual é {valor}')

    def sintonizacanal(self, valor):
        if valor not in self.list:
            self.list.append(valor)
            print(f'O canal {valor} foi adicionado')

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv

    def aumentaVolume(self, valor):
        self.tv.aumentaVolume(valor)

    def diminuirvolume(self):
        self.tv.diminuirvolume(90)

    def trocardecanal(self, valor):
        self.tv.trocardecanal(valor)

    def sintonizacanal(self,valor):
        self.tv.sintonizacanal(valor)