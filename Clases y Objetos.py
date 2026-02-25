# Clases y Objetos
# snake_case
# PascalCase para definir clases en python
class Celular:
  def __init__(self, marca, modelo, camara): #forma de referirse a si mismo
    self.marca = marca
    self.modelo = modelo
    self.camara = camara 
     
  
celular1 = Celular("Samsung","S23","48MP")

print(celular1.marca)