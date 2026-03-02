def decorador(funcion):
  def funcion_modificada():
    # aqui va todo lo que se ejecuta antes de llamar a la funcion original
    print("Antes de llamar a la funcion")
    funcion()
    print("Despues de llamar a la funcion")
    # aqui va todo lo que se ejecuta despues de llamar a la funcion original
  return funcion_modificada

# def saludo():
#   print("hola Valduz como estas?")
  
# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
  print("hola Valduz como estas?")
saludo()