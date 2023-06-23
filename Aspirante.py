from Usuario import *
class Aspirante(Usuario):
    def __init__(self, documento, nombre, correo, contraseña,telefono):
        Usuario.__init__(self, documento, nombre, correo, contraseña, telefono)
        self.__documento = documento
        self.__nombre  = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.__telefono = telefono
        self.__experiencia = []
        self.__educacion = []
    
    def setDocumento(self,documento):
        self.__documento = documento 
   
    def getDocumento(self):
        return self.__documento
    
    
    def setNombre(self,nombre):
        self.__nombre=nombre
             
    def getNombre(self):
        return self.__nombre
    
    
    def setCorreo(self,correo):
        self.__correo = correo
            
    def getCorreo(self):
        return self.__correo
    
    
    def setContraseña(self,contraseña):
        self.__contraseña = contraseña
        
    def getContraseña(self):
        return self.__contraseña
    
    
    def setTelefono(self,telefono):
        self.__telefono = telefono
         
    def getTelefono(self):
        return self.__telefono
    
    
    def agregarExperiencia(self,experiencia):
        self.__experiencia.append(experiencia)
        
    def agregarEducacion(self,educacion):
        self.__educacion.append(educacion)
    

