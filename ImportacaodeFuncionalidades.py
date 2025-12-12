from funcionalidades import *
tv = televisor('Sony', 'Sony3000')
controle = ControleRemoto(tv)
controle.sintonizacanal('SBT')
controle.trocardecanal('SBT')
print(tv.canalatual)
