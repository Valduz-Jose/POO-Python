# Principio de inversion de dependencias -> las clases de alto nivel no deben depender de las clases de bajo nivel, ambas deben depender de abstracciones. Esto significa que el diseño del sistema debe estar basado en interfaces o clases abstractas, y no en implementaciones concretas. De esta manera, se puede cambiar la implementación sin afectar a las clases que dependen de ella.

# class Diccionario:
#   def verificar_palabra(self,palabra):
#     # Logica para verificar palabras
#     pass
  
# class CorrectorOrtografico:
#   def __init__(self):
#     self.diccionario = Diccionario()
    
#   def corregir_texto(self,texto):
#     # usamos el diccionario para corregir el texto
#     pass
  
from ABC import ABC, abstractmethod

class VerificarOrtografia(ABC):
  @abstractmethod
  def verificar_palabra(self,palabra):
    # Logica para verificar palabras
    pass
  
class Diccionario(VerificarOrtografia):
  def verificar_palabra(self,palabra):
    # Logica para verificar palabras
    pass
  
# class ServicioOnline(VerificarOrtografia):
  
class CorrectorOrtografico:
  def __init__(self,diccionario):
    self.diccionario = diccionario
    
  def corregir_texto(self,texto):
    # usamos el diccionario para corregir el texto
    pass
  
corrector = CorrectorOrtografico(Diccionario())

