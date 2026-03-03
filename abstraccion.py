# manejar la complejidad ocultando datos innecesarios al usuario mostrando solo lo escencial, es decir, ocultar los detalle de implementacion y mostrar solo la funcionalidad
class Auto:
  def __init__(self):
    self._estado = "apagado"
    
  def encender(self):
    self._estado = "encendido"
    print("El auto esta encendido")
    
  def conducir(self):
    if self._estado == "apagado":
      self.encender()
    print("Conduciendo el auto")
    
mi_auto = Auto()
mi_auto.conducir()
# En este ejemplo, la clase Auto tiene un atributo privado _estado que indica si el auto está encendido o apagado. El método conducir() verifica el estado del auto y lo enciende si está apagado antes de permitir conducirlo. De esta manera, el usuario no necesita preocuparse por el estado del auto, ya que la clase se encarga de manejarlo internamente.