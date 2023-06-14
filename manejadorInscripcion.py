import numpy as np
from claseInscripcion import Inscripcion
class manejaIncripcion:
  def __init__(self):
    self.__lista = []
  def getarre(self,nombre,id):
    print("ingrese la fecha de la inscripcion")
    fecha=input("")
    pago=False
    self.__lista.append((fecha,pago,nombre,id))
    Inscripcion.setfecha(fecha)
    Inscripcion.setpago(pago)
    arre = np.array(self.__lista) 
    return arre
