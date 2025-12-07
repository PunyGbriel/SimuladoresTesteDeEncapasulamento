class main:
    pass

print('teste')
from Cliente import Cliente
from Conta import Conta

c1 = Cliente('Roberto', '99292929', 'Abrobra@Gmail.com')
d = Conta(c1.get_nome(), 1000, 0)
print(c1)

d.deposita(0)
d.saque(50)
d.extrato()