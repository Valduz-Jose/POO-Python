class Persona:
  def __init__(self,nombre,edad,nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad
    
  def hablar(self):
    print("Hola, estoy hablando")

class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario 
    
class Estudiante(Persona):
  def __init__(self, nombre, edad, nacionalidad,notas,universidad):
    super().__init__(nombre, edad, nacionalidad)
    self.notas = notas
    self.universidad = universidad 
    
class Artista:
  def __init__(self,habilidad):
    self.habilidad=  habilidad
  def mostrar_habilidad(self):
    return f"Mi habilidad es: {self.habilidad}"

class EmpleadoArtista(Persona,Artista):
  def __init__(self, nombre, edad, nacionalidad,habilidad, trabajo, salario):
    Persona.__init__(self,nombre,edad,nacionalidad)
    Artista.__init__(self,habilidad)
    self.trabajo=trabajo
    self.salario=salario
    
  def presentarse(self):
    print (f'Hola soy {self.nombre} y {super().mostrar_habilidad()} y trabajo como {self.trabajo}')
  
roberto = EmpleadoArtista("Roberto","43","argentino","Cantante","Programador",100000)

print(roberto.nombre)

roberto.presentarse()

herencia = issubclass(Artista,PermissionError)
instancia = isinstance(roberto,EmpleadoArtista)
print(herencia)
print(instancia)




