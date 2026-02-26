
class Estudiante:
  def __init__(self, nombre, edad, grado): 
    self.nombre = nombre
    self.edad = edad
    self.grado = grado 
  
  def estudiar(self):
    print("Estudiando..")
nombre = input("Digame su nombre: ")
edad = input("Digame su edad: ")
grado = input("Digame su gado: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      DATOS DEL ESTUDIANTE \n\n
      Nombre:{estudiante.nombre}
      Edad:{estudiante.edad}
      Grado:{estudiante.grado}
      """)

while True:
  
  estudiar = input()
  if(estudiar.lower() == "estudiar"):
    estudiante.estudiar()





