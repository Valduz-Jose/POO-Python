class Pato:
  def caminar(self):
    print ("Este pato esta caminando")
  
  def hablar(self):
    print ("Este pato esta haciendo cuack")
    
class Gallina:
  def caminar(self):
    print ("Esta Gallina esta caminando")
  
  def hablar(self):
    print ("Esta Gallina esta cacareando")
    
class Persona:
  def atrapar(self,pato):
    pato.caminar()
    pato.hablar()
    print("Lo Atrapaste!")
    
pato = Pato()
gallina = Gallina()
persona = Persona()

persona.atrapar(gallina)
# EN duck typing no importa el tipo de objeto, sino que tenga los metodos necesarios para realizar la tarea.
# Si camina como un pato y habla como un pato, entonces es un pato.