from abc import ABC, abstractmethod

class Persona(ABC):
  @abstractmethod
  def __init__(self,nombre, edad, sexo,actividad):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.actividad = actividad
    
  @abstractmethod
  def hacer_actividad(self):
    pass
  
  def presentarse(self):
    print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y soy {self.sexo}.")
    
# valduz = Persona("Alejandro", 27, "masculino","Programador")
# No se puede crear una instancia de la clase Persona porque es una clase abstracta. Para usarla, se debe crear una subclase que implemente el método abstracto trabajar().

class Estudiante(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)

  def hacer_actividad(self):
    print(f"Estoy estudiando {self.actividad}")

class Trabajador(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)

  def hacer_actividad(self):
    print(f"Estoy trabajando en {self.actividad}")
  
valduz = Estudiante("Alejandro", 27, "masculino","Programacion")
juan = Trabajador("Juan", 18, "masculino","Programacion")

valduz.presentarse()
valduz.hacer_actividad()
juan.presentarse()
juan.hacer_actividad()