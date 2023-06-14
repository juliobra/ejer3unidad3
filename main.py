from claseTaller import Taller

from manejaPersona import ManejaPersona

from manejadorInscripcion import manejaInscripcion

def test(self):
  taller=Taller()
  
  
  print("ingrese una opcion (Termine con 0)")
  
  print("1: Inscribir una persona en un taller: Se registra la inscripción (con el atributo pago en False) y la cantidad de vacantes del taller debe ser actualizada")
  print("2:Consultar inscripción: Ingresar el DNI de una persona, si está inscripta mostrar el nombre del taller en el que se inscribió y el monto que adeuda.")
  print("3:Consultar inscriptos: Ingresar el identificador de un taller y listar los datos de los alumnos que se inscribieron en él.")
  print("4:Registrar pago: Ingresar el DNI de una persona y registrar el pago (dar al atributo pago el valor True).")
  print("5:Guardar inscripciones: Generar un nuevo archivo que contenga los siguientes datos de las inscripciones: DNI de la persona, idTaller, fechaInscripcion y pago.")
  op=int(input(""))
  
  while op!=0:
    if op == 1:
      listataller= taller.cargaTaller()
      listaper= ManejaPersona(listataller)
      listains= manejaInscripcion()
      listaper.cargaPer(listains)
    if op==2:
      print("ingrese el dni para saber si esta insripta")
      dni=input("")
      listaper.buscadni(dni)


    if op==3:
      print("ingrese el id del taller para saber los inscriptos")
      
      

    if op==4:
      print("ingrese un dni para regitrar el pago")
      Dni=input("")

    if op==5:
      print("guardar inscripciones")
      
  
  
if __name__=='__main__':
  test()
  # 2.     Inscribir una persona en un taller: Se registra la inscripción (con el atributo pago en False) y la cantidad de vacantes del taller debe ser actualizada