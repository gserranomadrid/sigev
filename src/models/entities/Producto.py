class Producto:
    def __init__(self, id, codigo, nombre, descripcion, precio, stock, activo=1):
        self.__id = id
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__activo = activo

    def get_id(self):
        return self.__id
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_descripcion(self):
        return self.__descripcion
    def get_precio(self):
        return self.__precio
    def get_stock(self):
        return self.__stock
    def get_activo(self):
        return self.__activo
