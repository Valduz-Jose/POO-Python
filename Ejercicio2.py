class Persona:
  def __init__(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad
  
  def m_datos(self):
    print (f"El nombre es {self.nombre} y tiene {self.edad} a*os")
    
class Estudiante(Persona):
  def __init__(self, nombre, edad,grado):
    super().__init__(nombre, edad)
    self.grado=grado
    
  def datos(self):
    print (f"el grado es {self.grado}")
  
estudiante = Estudiante("Juan Marcos","18","Tercer Semestre")
estudiante.m_datos()
estudiante.datos()