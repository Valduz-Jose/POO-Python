# Clases y Objetos
# snake_case
# PascalCase para definir clases en python
class Celular:
  # Este es el metodo constructor necesario para crear atributos de instancia
  def __init__(self, marca, modelo, camara): #forma de referirse a si mismo
    self.marca = marca
    self.modelo = modelo
    self.camara = camara 
  
  def llamar(self):
    print(f'Estas Llamando desde un : {self.modelo}')   
  
  def cortar(self):
    print(f'cortaste la llamada desde tu : {self.modelo}')   
  
celular1 = Celular("Samsung","S23","48MP")
celular1.llamar()
celular1.cortar()
print(celular1.marca)