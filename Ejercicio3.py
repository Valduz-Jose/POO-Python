class Persona:
  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad
  
  def datos(self):
    print (f"El nombre es {self.nombre} y tiene {self.edad} años")
  
class Estudiante(Persona):
  def __init__(self,nombre,edad,grado):
    super().__init__(nombre,edad)
    self.grado=grado
  
  def datos(self):
    print (f"el grado es {self.grado}")

estudiante = Estudiante("Juan Marcos","18","Cuarto Semestre")
estudiante.datos()