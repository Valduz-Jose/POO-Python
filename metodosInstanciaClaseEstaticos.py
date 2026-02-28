class User:
  def __init__(self,username):
    self.username = username
    
  @classmethod
  def set_password(cls,password):
    return password+ " super algoritmo"  
  #Los metodos de clase le pertenecen a la clase y se caracterizan por usar un parametro del tipo cls, el cual hace referencia a la clase misma, es decir a la plantilla a partir de la cual se crean los objetos.
  # se usa el @classmethod para indicar que el metodo es de clase, y se puede llamar sin necesidad de crear una instancia de la clase, es decir sin crear un objeto a partir de la clase.
  
  def update(self,username,password):
    self.username = username
    self.password = password
    self.__save()
    
  
  def say_hello(self):
    print(f"Hola, mi username es {self.username}")
    # Los metodos de instancia le pertenecen a la instancia se caracterizan por usar un parametro del tipo self, el cual hace referencia a la instancia misma, es decir a un objeto creado a partir de la clase.
    # Los metodos de instancias permiten acceder a los atributos de la instancia y modificar su estado, ademas de realizar acciones relacionadas con la instancia.
  @staticmethod
  def area(radio):
      return 3.1415 * float(radio ^ 2)
    # Metodos estaticos pueden ser usados directamente por la clase pero no le pertenecen a la clase ni a la instancia, es decir no tienen acceso a los atributos de la clase ni de la instancia, se caracterizan por no usar ni el parametro cls ni el parametro self, y se usan para realizar tareas relacionadas con la clase pero que no necesitan acceder a los atributos de la clase ni de la instancia. Se usan con el decorador @staticmethod.
    
  def __save(self):
    pass
User.area(10)