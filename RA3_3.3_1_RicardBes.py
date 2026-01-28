# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 21/01/2026
# Versió: 1
#
# Descripció: Converteix un codi amb alt acoplament en un de baix acoplament mitjançant injecció de dependències i delegació de responsabilitats.
# Especificacions d'Entrada: Factura no creï la impressora, sinó que la rebi des de fora. Es pugui canviar el tipus d’impressora sense modificar la classe Factura.


# Antic
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class Factura:
    def __init__(self, client, import_total):
        self.client = client
        self.import_total = import_total
        self.impressora = ImpressoraPDF()  # Acoplament directe

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {slef.import_total} €"
        self.impressora.imprimir.imprimir(contingut)

# Nou
class ImpressoraPDF:
    def imprimir(self, contingut):
        print(f"Imprimint PDF: {contingut}")

class Factura:
    def __init__(self, client):
        self.client = client
        self.impressora = ImpressoraPDF 

    def imprimir_factura(self):
        contingut = f"Factura per a {self.client}, total: {slef.import_total} €"
        self.impressora.imprimir.imprimir(contingut)