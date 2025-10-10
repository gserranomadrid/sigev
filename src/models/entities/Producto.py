class Producto:
    def __init__(self, id, codigo, nombre, descripcion, precio, stock, activo=1):
        self.__id = id
        self.__codigo = codigo
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio = precio
        self.__stock = stock
        self.__activo = activo
