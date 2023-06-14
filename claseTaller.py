 
import csv
class Taller:
  def __init__(self,idtaller, nombre, vacantes, montoinscripcion):
    self.__idtaller= idtaller
    self.__nombre= nombre
    self.__vacantes= vacantes
    self.__montoinscripcion= montoinscripcion
  
  def cargaTaller (self):
   datos=[]
   archivo= open("talleres.csv")
   reader= csv.reader(archivo, delimiter= ',') 
   for fila in reader:
      idtaller= fila[0]
      nombre=fila[1]
      vacantes=fila[2]
      montoinscripcion=fila[3]
      datos.append(fila)
  def getnombre(self):
    return self.__nombre
   
  def setvacantes(self,u):
    self.__vacantes-= u   
    
                   
    
      
      
      