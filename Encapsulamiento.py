class MiClase:
  def __init__(self):
    self._atributo_privado = "valor"
    self.__atributo_Superprivado = "valor"
    # Atributo protegido: se puede acceder desde la clase y sus subclases, pero no desde fuera de la clase.
    # Atributo privado: se puede acceder solo desde la clase, no desde fuera de la clase ni desde subclases.
    # Atributo súper privado: se puede acceder solo desde la clase, no desde fuera de la clase ni desde subclases, y no se puede acceder a través de la sintaxis de acceso directo.
    
    def __hablar(self):
    # Método privado: se puede acceder solo desde la clase, no desde fuera de la clase ni desde subclases.
      print("Hola")
    
objeto = MiClase()
# print(objeto._atributo_privado)

class Persona:
  def __init__(self,nombre,edad):
    self.__nombre = nombre
    self._edad = edad
    
  def get_nombre(self):
    return self.__nombre
  
  def set_nombre(self,new_nombre):
    self.__nombre = new_nombre
    
  
alejo = Persona("Alejo",26)
nombre = alejo.get_nombre()
print(nombre)
alejo.set_nombre("Alejandro")
nombre = alejo.get_nombre()
print(nombre)



