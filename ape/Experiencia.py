class Experencia:
    def __init__(self,fecha_inicio,fecha_fin,empresa,funciones):
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__empresa = empresa
        self.__funciones = funciones
        
    
    def setfecha_inicio(self,fecha_inicio):
        self.__fecha_inicio=fecha_inicio
    def getfecha_inicio(self):
        self.__fecha_inicio
        
    def setfecha_fin(self,fecha_fin):
        self.__fecha_fin=fecha_fin
    def getfecha_fin(self):
        self.__fecha_fin
        
    def setempresa(self,empresa):
        self.__empresa=empresa
    def getempresa(self):
        self.__empresa
        
    def setfunciones (self,funciones):
        self.__funciones=funciones
    def getfunciones (self):
        self.__funciones
        
        
    