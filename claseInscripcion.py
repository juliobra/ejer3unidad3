

class Inscripcion: 
  __fechaincripcion: str
  __pago: bool
  def __init__(self, fechainscripcion, pago):
    self.__fechainscripcion= fechainscripcion
    self.__pago= pago
  def setfecha(self, fecha):
    self.__fechaincripcion=fecha
  def setpago(self, pago):
    self.__pago=pago
    


  