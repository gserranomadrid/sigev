class Proveedor:
    def __init__(self, id, rif, razon_social, telefono, email, activo=1):
        self.__id = id
        self.__rif = rif
        self.__razon_social = razon_social
        self.__telefono = telefono
        self.__email = email
        self.__activo = activo

    def get_id(self):
        return self.__id
    def get_rif(self):
        return self.__rif
    def get_razon_social(self):
        return self.__razon_social
    def get_telefono(self):
        return self.__telefono
    def get_email(self):
        return self.__email
    def get_activo(self):
        return self.__activo
