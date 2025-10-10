class Cliente:
    def __init__(self, id, documento, tipo_documento, razon_social, telefono, email):
        self.__id = id
        self.__documento = documento
        self.__tipo_documento = tipo_documento
        self.__razon_social = razon_social
        self.__telefono = telefono
        self.__email = email
        self.__activo = 1  # Nuevo atributo para estado activo/inactivo

    def get_id(self):
        return self.__id
    def get_documento(self):
        return self.__documento
    def get_tipo_documento(self):
        return self.__tipo_documento
    def get_razon_social(self):
        return self.__razon_social
    def get_telefono(self):
        return self.__telefono
    def get_email(self):
        return self.__email
    def get_activo(self):
        return self.__activo