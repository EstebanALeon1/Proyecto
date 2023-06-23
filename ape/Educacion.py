class Educacion :
    def __init__(self,lugar,tiempo,logro_alcanzado,doc_certificacion):
        self.__lugar = lugar
        self.__tiempo = tiempo
        self.__logro_alcanzado = logro_alcanzado
        self.__doc_certificacion = doc_certificacion
        
    def setlugar(self,lugar):
        self.__lugar = lugar
    def getlugar(self):
        self.__lugar 