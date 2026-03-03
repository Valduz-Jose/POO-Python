# ISP ningun cliente debe ser forzado a depender de interfaces que no utiliza. Esto significa que una clase no debe implementar metodos que no necesita o que no va a utilizar. En su lugar, se deben crear interfaces mas especificas y enfocadas en las necesidades de cada cliente.

from abc import ABC, abstractmethod

class Trabajador(ABC):
  
  @abstractmethod
  def trabajar(self):
    pass
  
class Comedor(ABC):
  @abstractmethod
  def comer(self):
    pass
  
class Dormilon(ABC):
  @abstractmethod
  def dormir(self):
    pass
  
class Humano(Trabajador,Comedor,Dormilon):
  def comer(self):
    print("El Humano esta comiendo")
    
  def trabajar(self):
    print("El humano esta trabajando")
    
  def dormir(self):
    print("El humano esta durmiendo")
    
class Robot(Trabajador):
  def trabajar(self):
    print("El Robot esta trabajando")
    
  
robot = Robot()
robot.trabajar()

Humano = Humano()
Humano.comer();