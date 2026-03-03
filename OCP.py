# Principio de abierto/cerrado -> las clases deben estar abiertas para su extension pero cerradas para su modificacion. Esto significa que el comportamiento de una clase debe poder ser extendido sin modificar su codigo fuente.
# Esto se puede lograr utilizando la herencia, la composicion o el uso de interfaces.
class Notificador:
  def __init__(self,usuario,mensaje):
    self.usuario = usuario
    self.mensaje = mensaje
    
  def notificar(self):
    raise NotImplementedError
  
  
class NotificadorEmail(Notificador):
  def Notificar(self):
    print(f"Enviando email a {self.usuario} con el mensaje: {self.mensaje}")
    
class NotificadorSMS(Notificador):
  def Notificar(self):
    print(f"Enviando SMS a {self.usuario} con el mensaje: {self.mensaje}")
    
    
class NotificadorWhatsapp(Notificador):
  def Notificar(self):
    print(f"Enviando WhatsApp a {self.usuario} con el mensaje: {self.mensaje}")
    
    
    
    