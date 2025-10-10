class Proveedor:
    def __init__(self, id, rif, razon_social, telefono, email, activo=1):
        self.__id = id
        self.__rif = rif
        self.__razon_social = razon_social
        self.__telefono = telefono
        self.__email = email
        self.__activo = activo
