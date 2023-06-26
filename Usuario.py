class Usuario:
    aspirantelista = []
    empresalista = []
    def __init__(self,documento, nombre, correo, contraseña, telefono, ubicacion):
        self.__documento = documento
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña
        self.__telefono = telefono
        self.__ubicacion = ubicacion
        
        self.__empresa = []




    def componerEmpresa(self):
        documento=input('Ingrese el numero de documento de la empresa: ')
        nombre=input('Ingrese el nombre de la empresa: ')
        correo=input('Ingrese el correo empresarial: ')
        contraseña=input('Cree su contraseña: ')
        telefono=input('Ingrese el telefono de su empresa: ')
        ubicacion =input('Ingrese la ubicacion: ')
        objempresa=Empresa(documento, nombre, correo, contraseña, telefono, ubicacion)
        self.__oferta.append(objempresa)

    def verEmpresa(self):
        return self.__empresa