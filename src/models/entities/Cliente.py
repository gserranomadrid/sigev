class Cliente:
    def __init__(self, id, documento, tipo_documento, razon_social, telefono, email):
        self.__id = id
        self.__documento = documento
        self.__tipo_documento = tipo_documento
        self.__razon_social = razon_social
        self.__telefono = telefono
        self.__email = email
        self.__activo = 1  # Nuevo atributo para estado activo/inactivo