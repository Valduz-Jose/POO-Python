# Las clases derivadas deben ser sustituibles por sus clases base sin alterar el correcto funcionamiento del programa. Esto significa que si una clase A es una subclase de una clase B, entonces los objetos de la clase A deben poder reemplazar a los objetos de la clase B sin afectar el comportamiento del programa.

# class Ave:
#   def volar(self):
#     return "Estoy Volando"
  
# class Pinguino(Ave):
#   def volar(self):
#     return "No puedo volar"

# def hacer_volar(ave = Ave):
#   return ave.volar()

# print(hacer_volar(Pinguino()))

class Ave:
  pass

class AveVoladora(Ave):
  def volar(self):
    return "Estoy Volando"
  
class AveNoVoladora(Ave):
  pass

