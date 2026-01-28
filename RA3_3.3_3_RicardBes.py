# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 21/01/2026
# Versió: 1
#
# Descripció: Refés el codi perquè la lògica de descompte no estigui codificada dins CarretCompra. Has de:
# Especificacions d'Entrada: Crear una classe Descompte20 amb un mètode aplicar(total). Fer que CarretCompra rebi l’estratègia de descompte al constructor.

# Antic
class CarretCompra:
    def __init__(self, total):
        self.total = total

    def calcular_total_amb_descompte(self):
        descompte = self.total * 0.2 # 20% fix
        return self.total - descompte

# Nou
class Descompte20:
    def aplicar(total):
    return preu * 0.90

class CarretCompra:
    def __init__(self, total):
        self.total = total

    def calcular_total_amb_descompte(self):
        descompte = self.total * 0.2 # 20% fix
        return self.total - descompte