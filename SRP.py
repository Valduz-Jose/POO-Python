# S -> cada clase debe encargarse de una sola cosa, funcionalidad unica, y esa funcionalidad debe estar completamente encapsulada por la clase.
class TanqueDeCombustible:
  def __init__(self):
    self.combustible = 100
  
  def agregar_combustible(self, cantidad):
    self.combustible += cantidad
    
  def obtener_combustible(self):
    return self.combustible
  
  def usar_combustible(self, cantidad):
    self.combustible -= cantidad
  
class Auto():
  def __init__(self,tanque):
    self.posicion = 0
    # self.combustible = 100
    self.tanque = tanque
    
  def mover(self,distancia):
    if self.tanque.obtener_combustible() >= distancia/2:
      self.posicion += distancia
      self.tanque.usar_combustible (distancia/2)
      print("Se ha movido exitosamenre")
    else:
      print("No hay suficiente combustible para moverse esa distancia")
      
  def obtener_posicion(self):  
    return self.posicion
      
  
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
print(autito.mover(10))
print(autito.obtener_posicion())
print(autito.mover(20))
print(autito.obtener_posicion())
print(autito.mover(60))
print(autito.obtener_posicion())
print(autito.mover(100))
print(autito.obtener_posicion())
print(autito.mover(120))
print(autito.obtener_posicion())