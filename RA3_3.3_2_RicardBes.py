# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 21/01/2026
# Versió: 1
#
# Descripció: Refés el codi perquè la classe Comanda no depengui d’una implementació concreta del notificador. El notificador ha de ser passat com a dependència al constructor.
# Especificacions d'Entrada: 

# Antic
class EmailNotificador:
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

class Comanda:
    def __init__(self, client):
         self.client = client
         self.notificador = EmailNotificador() # Alt acoplament
    
    def confirmar(self):
         print(f"Comanda confirmada per {self.client}")
         self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")

# Nou
class EmailNotificador:
   def enviar(self, missatge):
      print(f"Enviant email: {missatge}")

class SMSNotificador:
   def enviar(self, missatge):
      print(f"Enviant SMS: {missatge}")

class Comanda:
   def __init__(self, client, notificador):
       self.client = client
       self.notificador = notificador
    
   def confirmar(self):
       print(f"Comanda confirmada per {self.client}")
       self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")