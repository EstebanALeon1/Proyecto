class Experiencia:
    def __init__(self,empresa,descripcion,fecha_inicio,fecha_fin,cargo,funciones):
        self.__empresa = empresa
        self.__descripcion = descripcion
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__cargo = cargo
        self.__funciones = funciones
        
    def setEmpresa(self,empresa):
        self.__empresa = empresa
   
    def getEmpresa(self):
        return self.__empresa
    
    
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