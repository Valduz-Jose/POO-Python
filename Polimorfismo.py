class Gato:
  def sonido(self):
    return "Miau"
class Perro:
  def sonido(self):
    return "Guau"

def hacer_sonido(animal):
  print(animal.sonido())
  
gato = Gato()
perro = Perro()

hacer_sonido(perro)

print(gato.sonido())
# Se puede hacer de esta manera ya que Python es un 
# lenguaje de tipado dinamico