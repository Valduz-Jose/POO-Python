class Persona:
  def __init__(self,nombre,edad):
    self.nombre = nombre
    self.edad = edad

  def __str__(self):
    return f"Nombre: {self.nombre}, Edad: {self.edad}"
  
  def __repr__(self):
    return f"Persona(nombre='{self.nombre}', edad={self.edad})"
  
  def __add__(self, other):
    nuevo_valor = self.edad + other.edad
    return Persona(self.nombre+other.nombre, nuevo_valor)
  
valduz = Persona("Alejandro",27)
print(valduz) # Al imprimir el objeto valduz, se llama automáticamente al método __str__() para obtener una representación legible del objeto. En este caso, se muestra el nombre y la edad de la persona.
repre = repr(valduz) # Al llamar a repr(valduz), se obtiene una representación más detallada del objeto, que incluye el nombre de la clase y los valores de los atributos. Esto es útil para depuración y desarrollo, ya que proporciona información más completa sobre el objeto.
print(repre)
resultado = eval(repre) # Al usar eval() con la representación obtenida de repr(valduz), se crea un nuevo objeto Persona con los mismos atributos que el objeto original. Esto demuestra cómo __repr__() puede ser utilizado para recrear objetos a partir de su representación.4
print(resultado) # Al imprimir el nuevo objeto resultado, se llama nuevamente al método __str__() para mostrar su representación legible. En este caso, se muestra el mismo nombre y edad que el objeto original valduz.
otro = Persona("Dalto",33)
maria = Persona("Maria",15)
nueva_persona = valduz + otro + maria # Al usar el operador + entre dos objetos Persona, se llama al método __add__() para definir cómo se deben combinar los objetos. En este caso, se crea un nuevo objeto Persona con el nombre concatenado de ambos objetos y la suma de sus edades.
print(nueva_persona.nombre)
