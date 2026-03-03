
class Persona:
  def __init__(self,nombre,edad):
    self.__nombre = nombre
    self._edad = edad
    
  @property
  def nombre(self): 
    return self.__nombre
# al usar @property, el método se puede llamar como un atributo, sin paréntesis.
  
  @nombre.setter
  def nombre(self,nuevo_nombre):
    self.__nombre = nuevo_nombre
  
  @nombre.deleter
  def nombre(self):
    del self.__nombre
    
alejo = Persona("Alejo",26)

nombre = alejo.nombre
print(nombre)

alejo.nombre = "Juan"

nombre = alejo.nombre
print(nombre)

del alejo.nombre

nombre = alejo.nombre
print(nombre)


# De esta forma es una codificacion mas limpia, ya que no se accede directamente a los atributos privados, sino a través de métodos que controlan el acceso a ellos. Esto permite validar los datos antes de asignarlos o realizar acciones adicionales al obtener o eliminar el valor.