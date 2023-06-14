import numpy as np
from clasePersona import Persona
from manejadorInscripcion import manejaIncripcion

class ManejaPersona:
  def __init__(self,listataller):
    self.__listaPer=[]
    self.__Arreglotalller= np.array(listataller)
  def cargaPer(self,incripcion):
    print("ingrese el nombre de la persona")
    nom=input("")
    Persona.setNombre(nom)
    print("ingrese direccion de la persona")
    direcc=input("")
    Persona.setdireccion(direcc)
    print("ingrese el dni de la persona")
    Dni=input("")
    Persona.setdni(Dni)
    unapersona=Persona(nom, direcc, Dni)
    self.__listaPer.append(unapersona)
    print("ingrese el nombre del taller al que desea incribirse la persona")
    nombre=input("")
    i=0
    while i< len(self.__Arreglotaller):
      if self.__Arreglotaller[i].getnombre() == nombre:
       
        print("el nombre del taller es {}".format(self.__Arreglotaller[i].getnombre()))
        self.__Arreglotaller[i].setvacantes(1)
      else:
        i+=1
    
  def buscadni(self,dni):
    i=0
    while i < len(self.__listaPer):
      if self.__listaPer[i].getdni()== dni:
        if self.__listaPer[i].getnom()== arreglo.getnombre():
          print("taller {} , monto {}".format())
          
        
    
    
    
    
    
    
    
  
      
    
  